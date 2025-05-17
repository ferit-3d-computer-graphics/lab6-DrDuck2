import k3d
import numpy as np
import time
from matplotlib.cm import jet
from matplotlib.colors import Normalize

grid_size = 40
x = np.linspace(-3, 3, grid_size)
y = np.linspace(-3, 3, grid_size)
X, Y = np.meshgrid(x, y)
Z = 0.5 * np.sin(X**2 + Y**2)  

vertices = np.stack([X.ravel(), Y.ravel(), Z.ravel()], axis=1).astype(np.float32)

faces = []
for i in range(grid_size-1):
    for j in range(grid_size-1):
        idx = i * grid_size + j
        faces.append([idx, idx+1, idx+grid_size])
        faces.append([idx+1, idx+grid_size+1, idx+grid_size])
faces = np.array(faces, dtype=np.uint32)

plot = k3d.plot()
temperature = np.zeros_like(Z.ravel()) 
mesh = k3d.mesh(vertices, faces, colors=[] , wireframe=False, flat_shading=False)
plot += mesh
plot.display()

cmap = jet
norm = Normalize(vmin=-1, vmax=1)

for t in range(100):
    temperature = np.sin(X.ravel() + t*0.2) * np.cos(Y.ravel() + t*0.15) + 0.3*np.random.randn(*X.ravel().shape)
    
    colors = (cmap(norm(temperature))[:, :3] * 255).astype(np.uint32)
    hex_colors = (colors[:, 0] << 16) | (colors[:, 1] << 8) | colors[:, 2]
    
    mesh.colors = hex_colors.astype(np.uint32)
    
    time.sleep(0.05)