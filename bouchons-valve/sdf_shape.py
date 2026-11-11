#!/usr/bin/env python3
"""Forme « douce » des bouchons croix, en champ de distance signé (SDF, mm).

Repère : x horizontal, y profondeur (épaisseur de l'anneau), z vertical vers le BAS
(z = 0 au sommet, comme sur les croquis). Négatif = matière.
Les raccords sont obtenus par union lissée (smooth-min) : pas d'arête entre
le tube, l'anneau et la barre.
"""
import json, sys, pathlib
import numpy as np

TOP_R, BOT_R = 1.6, 0.8     # arrondis du tube (sommet, pied)
RING_DEPTH = 6.0            # épaisseur de l'anneau et de la barre (axe y)
EDGE_R = 1.0                # arrondi des arêtes de l'anneau et de la barre
BAR_H = 3.0                 # hauteur de la barre horizontale
# rayon de raccord entre volumes : voir params() (1,2 mm grande croix, 0,8 mm petite)
TOPWALL = 1.5

STYLES = {
    # version « subtile » validée : anneau 6 mm d'épaisseur, arêtes R 1
    "subtil":  dict(depth=6.0, edge=1.0, band=(2.6, 2.2), bar=(3.0, 3.0), blend=(1.2, 0.8), top_r=1.6),
    # version « affirmée » : plus épaisse vers l'avant/arrière (ne mange pas les fenêtres),
    # sections presque rondes, raccords plus larges
    "affirme": dict(depth=8.0, edge=1.5, band=(3.0, 2.5), bar=(3.4, 3.0), blend=(1.8, 1.0), top_r=2.4),
    # anneau plus grand, aussi épais que le tube (≈ Ø 12) : un seul volume continu
    "epouse":  dict(depth=12.0, edge=1.5, band=(3.0, 2.5), bar=(3.4, 3.0), blend=(1.8, 1.0), top_r=2.4, dmax=29.0),
    # même pièce, sommet coupé net à plat : posé directement sur le plateau, sans supports
    "plat":    dict(depth=12.0, edge=1.5, band=(3.0, 2.5), bar=(3.4, 3.0), blend=(1.8, 1.0), top_r=0.0, dmax=29.0, flat=True),
}
STYLE = "subtil"

def params(H, style=None):
    st = STYLES[style or STYLE]
    L = H - 0.5
    D = min(L, st.get("dmax", 26.0))
    big = D >= 26
    band = st["band"][0 if big else 1]
    RO = D / 2
    return dict(L=L, RO=RO, band=band, Rmid=RO - band / 2, cy=RO, blend=st["blend"][0 if big else 1],
                depth=st["depth"], edge=st["edge"], bar=st["bar"][0 if big else 1], top_r=st["top_r"],
                flat=st.get("flat", False))

def smin(a, b, k):
    h = np.clip(0.5 + 0.5 * (b - a) / k, 0.0, 1.0)
    return b * (1 - h) + a * h - k * h * (1 - h)

def smax(a, b, k):
    return -smin(-a, -b, k)

def rbox2(px, py, hx, hy, r):
    qx = np.abs(px) - hx + r
    qy = np.abs(py) - hy + r
    return np.hypot(np.maximum(qx, 0), np.maximum(qy, 0)) + np.minimum(np.maximum(qx, qy), 0) - r

def rbox3(px, py, pz, hx, hy, hz, r):
    qx, qy, qz = np.abs(px) - hx + r, np.abs(py) - hy + r, np.abs(pz) - hz + r
    out = np.sqrt(np.maximum(qx, 0) ** 2 + np.maximum(qy, 0) ** 2 + np.maximum(qz, 0) ** 2)
    return out + np.minimum(np.maximum(np.maximum(qx, qy), qz), 0) - r

def tube_radius(z):
    return 5.8 + 0.5 * np.clip(z, 0, None) / 31.5

def body(x, y, z, H):
    p = params(H)
    L = p["L"]
    rad = np.hypot(x, y)
    r_round = np.where(z < L / 2, p["top_r"], BOT_R)
    tube = rbox2(rad, z - L / 2, tube_radius(z), L / 2, r_round)
    q = np.hypot(x, z - p["cy"]) - p["Rmid"]
    ring = rbox2(q, y, p["band"] / 2, p["depth"] / 2, min(p["edge"], p["band"] / 2 - 0.05))
    bar = rbox3(x, y, z - p["cy"], p["Rmid"], p["depth"] / 2, p["bar"] / 2, min(p["edge"], p["bar"] / 2 - 0.05))
    d = smin(smin(tube, ring, p["blend"]), bar, p["blend"])
    # le raccord lissé gonfle un peu là où l'anneau rejoint le haut/bas du tube :
    # intersection douce avec les plans z = 0 et z = L pour garder la hauteur exacte
    k = 0.6
    d = np.maximum(d, -z) if p["flat"] else smax(d, -(z + k / 4), k)
    d = smax(d, z - (L + k / 4), k)
    return d

def bore(x, y, z, H):
    """Alésage simplifié (le taraudage réel est soustrait plus tard en CSG)."""
    L = params(H)["L"]
    rad = np.hypot(x, y)
    thr = np.maximum(rad - 4.0, np.maximum(TOPWALL - z, z - 9.05))
    r_low = 4.8 + 0.2 * (z - 9.05) / max(L - 9.05, 1e-6)
    low = np.maximum(rad - r_low, np.maximum(9.05 - z, z - (L + 1)))
    return np.minimum(thr, low)

# ---------- contours 2D pour les croquis ----------
def contours(field, xs, zs):
    from skimage import measure
    out = []
    for c in measure.find_contours(field, 0.0):
        # c[:,0] -> indice z (lignes), c[:,1] -> indice x (colonnes)
        X = np.interp(c[:, 1], np.arange(len(xs)), xs)
        Z = np.interp(c[:, 0], np.arange(len(zs)), zs)
        out.append([[round(float(a), 3), round(float(b), 3)] for a, b in zip(X[::2], Z[::2])])
    return out

def sketch_data(H, step=0.04):
    p = params(H)
    L, RO = p["L"], p["RO"]
    xs = np.arange(-RO - 1.5, RO + 1.5, step)
    zs = np.arange(-2.0, L + 1.5, step)
    X, Z = np.meshgrid(xs, zs)
    Y0 = np.zeros_like(X)
    b = body(X, Y0, Z, H)
    front = contours(b, xs, zs)
    section = contours(np.maximum(b, -bore(X, Y0, Z, H)), xs, zs)
    # vue de dessus : projection selon z
    xt = np.arange(-RO - 1.5, RO + 1.5, step)
    yt = np.arange(-8.0, 8.0, step)
    Xt, Yt = np.meshgrid(xt, yt)
    top = np.full(Xt.shape, np.inf)
    for zv in np.arange(0.0, L + 1e-9, 0.1):
        top = np.minimum(top, body(Xt, Yt, np.full_like(Xt, zv), H))
    side_c = contours(top, xt, yt)
    return dict(H=H, **p, front=front, section=section, side=side_c)

if __name__ == "__main__":
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "sketch_soft.json")
    data = {}
    for st in STYLES:
        STYLE = st
        globals()["STYLE"] = st
        for H in (22, 32):
            data[f"{st}_{H}"] = sketch_data(H)
    out.write_text(json.dumps(data))
    print("ok", out, {k: (len(v["front"]), len(v["section"]), len(v["side"])) for k, v in data.items()})
