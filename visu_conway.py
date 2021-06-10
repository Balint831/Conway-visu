
import matplotlib.pyplot as plt
from read_conway import *
from matplotlib.animation import FuncAnimation

numSteps = 600

cpu = r"C:\Users\balin\source\repos\Conway-cpu-parallelize\conway_cpu_parallel\cnw_visu.txt"
gpu = r"C:\Users\balin\source\repos\Conway_GPU_solution\Conway_GPU_project\cnw_gpu_visu.txt"

grid = load_conway_file(gpu, numSteps, 20)

def anim(i, ax):
        ax.clear()
        plt.imshow(grid[i], cmap="gray")
        
        plt.title(f"Iteration number: {i}")



fig, ax = plt.subplots(figsize=[8,8])
ani = FuncAnimation(fig, anim, interval = 150, fargs = [ax],
        repeat = False, save_count = numSteps, frames = np.arange(numSteps))
ani.save('docs/GPU/blinker.gif', writer='ffmpeg',fps = 4)
plt.show()