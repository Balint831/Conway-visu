import numpy as np
from os import remove

def load_conway_file(fname, num_of_steps, dim):
    f = open(fname)

    lines = f.readlines()

    f.close()

    parsed_lines = [*map( lambda x: x.replace("\n", ""), lines)]


    for i in range(num_of_steps):
        parsed_lines.remove("")

    removed_empties = [*map( lambda x: x.replace(" ", ""), parsed_lines)]

    split_lines = [*map( lambda x: [*x], removed_empties)]

    arr = np.array(split_lines).astype(int)

    arr = arr.reshape(-1,dim,dim)

    return arr



if __name__ == "__main__":
    print(load_conway_file( r"C:\Users\balin\source\repos\Conway-cpu-parallelize\conway_cpu_parallel\cnw_visu.txt" , 20, 6))