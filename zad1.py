import k3d
import numpy as np
import time

t = np.linspace(0, 2 * np.pi, 100)
scale = 1.5  

x = scale * np.sin(t)
y = scale * np.sin(2 * t) * 0.8  
z = 0.5 * np.cos(t)  

trajectory = np.stack([x, y, z], axis=1).astype(np.float32)

plot = k3d.plot()

path_line = k3d.line(trajectory, width=0.05, color=0x666666)
plot += path_line

moving_point = k3d.points([trajectory[0]], 
                         point_size=0.3, 
                         color=0xff0000,
                         shader='3d')
plot += moving_point

plot.display()

for pos in trajectory:
    moving_point.positions = np.array([pos], dtype=np.float32)
    time.sleep(0.03)