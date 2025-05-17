import k3d
import numpy as np
import time
from matplotlib.colors import Normalize

plot = k3d.plot(grid_visible=True, axes_helper=0)
plot.camera = [5, 5, 5, 0, 0, 0, 0, 0, 1]

grid_size = 5
x_pos = np.linspace(-2, 2, grid_size)
y_pos = np.linspace(-2, 2, grid_size)
X, Y = np.meshgrid(x_pos, y_pos)

origins = np.stack([X.ravel(), Y.ravel(), np.zeros(grid_size**2)], axis=1).astype(np.float32)
heights = np.random.uniform(0.5, 2.5, size=grid_size**2)
directions = np.stack([np.zeros(grid_size**2), np.zeros(grid_size**2), heights], axis=1).astype(np.float32)

norm = Normalize(vmin=0, vmax=3)
bars = k3d.vectors(
    origins=origins,
    vectors=directions,
    attribute=heights,
    color_map=k3d.colormaps.matplotlib_color_maps.Viridis,  # Correct reference
    color_range=[0, 3],
    line_width=0.1,
    head_size=1.5
)

plot += bars

plot += k3d.text2d("3D Time Series Dashboard", position=[0.05, 0], size=1.5, color=0x000000)
color_legend = k3d.text2d("Value Scale\n0.0 (low) → 3.0 (high)", position=[0.6, 0.8], size=1.0, color=0x000000)
plot += color_legend

plot.display()

for t in range(100):
    phase = t * 0.1
    heights = 1.5 * np.sin(phase + X.ravel()*0.5 + Y.ravel()*0.3) + 1.5
    heights += 0.3 * np.random.randn(*heights.shape)
    
    directions[:, 2] = heights
    bars.vectors = directions.astype(np.float32)
    bars.attribute = heights
    
    current_max = f"Current Max: {heights.max():.2f}"
    color_legend.text = f"Value Scale\n0.0 (low) → 3.0 (high)\n{current_max}"
    
    time.sleep(0.1)
