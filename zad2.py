import k3d
import numpy as np
import time

grid_size = 5
x, y, z = np.meshgrid(np.linspace(-2, 2, grid_size),
                     np.linspace(-2, 2, grid_size),
                     np.linspace(-2, 2, grid_size))
origins = np.stack([x.ravel(), y.ravel(), z.ravel()], axis=1).astype(np.float32)

theta = np.arctan2(y, x).ravel()
initial_directions = np.stack([
    np.sin(theta),
    np.cos(theta),
    z.ravel() * 0.5
], axis=1).astype(np.float32)

plot = k3d.plot()
vectors = k3d.vectors(
    origins=origins,
    vectors=initial_directions,
    color=0x00FF00,
    line_width=0.05,
    head_size=1.2
)
plot += vectors
plot.display()

for t in range(100):
    phase = t * 0.2
    dx = np.sin(phase + x*0.5 + y*0.3).ravel()
    dy = np.cos(phase + y*0.4 + z*0.2).ravel()
    dz = np.sin(phase*0.5 + z*0.3 + x*0.4).ravel()
    
    # Combine components and scale
    new_directions = np.stack([dx, dy, dz], axis=1) * 0.5
    vectors.vectors = new_directions.astype(np.float32)
    
    time.sleep(0.05)
