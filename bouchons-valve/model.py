#!/usr/bin/env python3
"""Bouchons de valve « croix » — génération STL (mm).

Repère : axe de la valve = Z. Orientation d'impression : ouverture vers le HAUT
(pas d'effet ventouse en résine), sommet du bouchon vers le plateau.
Coordonnées construites comme sur les croquis (y du dessin = z ici), puis posées à z >= 0.
"""
import math, struct, sys, pathlib
import numpy as np
from manifold3d import Manifold, Mesh, set_circular_segments

set_circular_segments(128)
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")

# ---------- filetage valve 8V1 : 0.305"-32 UNEF ----------
P = 25.4 / 32            # 0.79375 mm
R_MAJ = 8.00 / 2         # fond du taraudage (valve : crête Ø 7,72 max) -> jeu 0,28 au diamètre
R_MIN = 7.15 / 2         # sommet du taraudage (valve : fond Ø ~6,9) -> jeu ~0,25 au diamètre
DEPTH = R_MAJ - R_MIN
FLANK = DEPTH * math.tan(math.radians(30))   # longueur axiale d'un flanc à 60°
CREST = (P - 2 * FLANK) / 2

def profile(s):
    """Rayon du 'négatif' (forme d'une vis mâle) en fonction de la phase axiale s ∈ [0,P)."""
    if s < CREST: return R_MAJ
    s -= CREST
    if s < FLANK: return R_MAJ - DEPTH * s / FLANK
    s -= FLANK
    if s < CREST: return R_MIN
    s -= CREST
    return R_MIN + DEPTH * s / FLANK

def thread_negative(z0, z1, n_theta=144, dz=P / 24):
    """Vis mâle pas à droite, de z0 à z1, à soustraire du corps -> taraudage."""
    nz = max(2, int(math.ceil((z1 - z0) / dz)) + 1)
    zs = np.linspace(z0, z1, nz)
    th = np.linspace(0, 2 * math.pi, n_theta, endpoint=False)
    verts = []
    for z in zs:
        for t in th:
            s = (z - P * t / (2 * math.pi)) % P     # hélice à droite
            r = profile(s)
            verts.append((r * math.cos(t), r * math.sin(t), z))
    verts.append((0, 0, z0)); verts.append((0, 0, z1))
    cb, ct = len(verts) - 2, len(verts) - 1
    tris = []
    idx = lambda i, j: i * n_theta + (j % n_theta)
    for i in range(nz - 1):
        for j in range(n_theta):
            a, b, c, d = idx(i, j), idx(i, j + 1), idx(i + 1, j), idx(i + 1, j + 1)
            tris += [(a, b, d), (a, d, c)]
    for j in range(n_theta):
        tris.append((cb, idx(0, j + 1), idx(0, j)))
        tris.append((ct, idx(nz - 1, j), idx(nz - 1, j + 1)))
    m = Manifold(Mesh(vert_properties=np.array(verts, np.float32), tri_verts=np.array(tris, np.uint32)))
    if m.volume() < 0 or m.is_empty():
        raise RuntimeError("négatif de filetage invalide")
    return m

# ---------- primitives ----------
def cyl_z(za, zb, ra, rb=None):
    rb = ra if rb is None else rb
    return Manifold.cylinder(zb - za, ra, rb).translate((0, 0, za))

RING_RO, RING_RI, RING_T = 13.0, 10.0, 6.0
TUBE_R = 5.5
BAR_W = 4.0

def cross_ring():
    ring = (Manifold.cylinder(RING_T, RING_RO, center=True) - Manifold.cylinder(RING_T + 1, RING_RI, center=True))
    ring = ring.rotate((90, 0, 0))                      # anneau dans le plan XZ
    bar = Manifold.cube((2 * 11.5, RING_T, BAR_W), center=True)
    return ring + bar

# ---------- Version A : coiffe courte ----------
def version_a():
    body = cross_ring() + cyl_z(-13, 13, TUBE_R)
    bore = thread_negative(5.5, 13.6)
    chamfer = cyl_z(12.3, 13.01, R_MIN, R_MAJ + 0.6)   # entrée chanfreinée
    return body - bore - chamfer

# ---------- Version B : manchon intégral ----------
def version_b(H):
    tip = -2.0
    bot = tip + H - 2.0                                 # s'arrête 2 mm au-dessus de la jante
    body = (cross_ring() + cyl_z(-13, 2.0, TUBE_R)
            + cyl_z(2.0, 5.0, TUBE_R, 6.9) + cyl_z(5.0, bot, 6.9, 8.8))
    bore = (thread_negative(tip - 0.5, tip + 7.05)
            + cyl_z(tip + 7.0, tip + 9.0, 5.1)              # collerette laiton
            + cyl_z(tip + 6.3, tip + 7.01, R_MIN, 4.3)      # amorce du filet
            + cyl_z(tip + 9.0, bot + 0.5, 5.4, 7.0))  # cône caoutchouc
    return body - bore

# ---------- export ----------
def to_print(m):
    lo = m.bounding_box()[:3]
    return m.translate((0, 0, -lo[2]))  # ouverture vers +Z, sommet sur z=0

def write_stl(m, path, name):
    mesh = m.to_mesh()
    v = np.asarray(mesh.vert_properties)[:, :3].astype(np.float64)
    t = np.asarray(mesh.tri_verts)
    a, b, c = v[t[:, 0]], v[t[:, 1]], v[t[:, 2]]
    n = np.cross(b - a, c - a)
    n /= np.maximum(np.linalg.norm(n, axis=1, keepdims=True), 1e-12)
    with open(path, "wb") as fh:
        fh.write(name.encode()[:80].ljust(80, b" "))
        fh.write(struct.pack("<I", len(t)))
        rec = np.zeros(len(t), dtype=[("n", "<f4", 3), ("a", "<f4", 3), ("b", "<f4", 3), ("c", "<f4", 3), ("x", "<u2")])
        rec["n"], rec["a"], rec["b"], rec["c"] = n, a, b, c
        fh.write(rec.tobytes())
    return len(t)

if __name__ == "__main__":
    parts = {
        "bouchon_croix_A_court.stl": version_a(),
        "bouchon_croix_B_long_H22.stl": version_b(22),
        "bouchon_croix_B_long_H32.stl": version_b(32),
    }
    for fname, m in parts.items():
        m = to_print(m)
        bb = m.bounding_box()
        ntri = write_stl(m, OUT / fname, fname)
        vol = m.volume() / 1000
        print(f"{fname}: {bb[3]-bb[0]:.2f} x {bb[4]-bb[1]:.2f} x {bb[5]-bb[2]:.2f} mm | "
              f"{vol:.2f} cm3 ≈ {vol*1.15:.1f} g résine | genus {m.genus()} | {ntri} tri | status {m.status()}")
