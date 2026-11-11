#!/usr/bin/env python3
"""Maillage de la version « douce » : SDF lissé -> marching cubes -> taraudage en CSG."""
import sys, pathlib
import numpy as np
from skimage import measure
from manifold3d import Manifold, Mesh
import sdf_shape as S
from model import thread_negative, cyl_z, write_stl, R_MIN

def body_mesh(H, step=0.08):
    p = S.params(H)
    L, RO = p["L"], p["RO"]
    xs = np.arange(-RO - 1.0, RO + 1.0 + step, step, dtype=np.float32)
    ys = np.arange(-8.5, 8.5 + step, step, dtype=np.float32)  # tube Ø ≤ 12,6 et anneau ≤ 8
    zs = np.arange(-1.5, L + 1.0 + step, step, dtype=np.float32)
    vol = np.empty((len(xs), len(ys), len(zs)), np.float32)
    X, Y = np.meshgrid(xs, ys, indexing="ij")
    for k, z in enumerate(zs):
        vol[:, :, k] = S.body(X, Y, np.full_like(X, z), H)
    verts, faces, _, _ = measure.marching_cubes(vol, 0.0, spacing=(step, step, step))
    verts += np.array([xs[0], ys[0], zs[0]], np.float32)
    m = Manifold(Mesh(vert_properties=verts.astype(np.float32), tri_verts=faces.astype(np.uint32)))
    if m.is_empty():
        raise RuntimeError(f"maillage invalide: {m.status()}")
    if m.volume() < 0:
        m = Manifold(Mesh(vert_properties=verts.astype(np.float32), tri_verts=faces[:, ::-1].astype(np.uint32)))
    return m, L

def soft_cap(H):
    m, L = body_mesh(H)
    bore = (thread_negative(S.TOPWALL, 9.1)
            + cyl_z(8.4, 9.06, R_MIN, 4.3)                    # amorce du filet
            + cyl_z(9.05, L + 0.5, 4.8, 5.0)                  # Ø 9,6 -> Ø 10
            + cyl_z(L - 0.6, L + 0.6, 5.0, 6.2))              # entrée adoucie
    return m - bore

if __name__ == "__main__":
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    style = sys.argv[2] if len(sys.argv) > 2 else "subtil"
    S.STYLE = style
    for H in (22, 32):
        m = soft_cap(H)
        lo = m.bounding_box()
        m = m.translate((0, 0, -lo[2]))
        m = m.simplify(0.01)                        # allège le maillage (écart ≤ 0,01 mm)
        bb = m.bounding_box()
        name = f"bouchon_croix_{style}_H{H}.stl"
        n = write_stl(m, out / name, name)
        print(f"{name}: {bb[3]-bb[0]:.2f} x {bb[4]-bb[1]:.2f} x {bb[5]-bb[2]:.2f} mm | "
              f"{m.volume()/1000:.2f} cm3 | genus {m.genus()} | {n} tri | {m.status()}")
