import taichi as ti
import meshtaichi_patcher as Patcher

mesh = Patcher.load_mesh("bunny.mesh", relations=["CV"])
