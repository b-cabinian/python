# -*- coding: utf-8 -*-
"""
Author: Brian Cabinian
Description: Slow solution to Project Euler Problem 15. Attempts depth first
search of all paths from upper left to lower right.

Too slow to solve for 20 x 20 grid 

https://projecteuler.net/problem=15
"""

def find_all_paths(src, dest, g, cur_path, all_paths):
    if src == dest:
        all_paths.append(cur_path.copy())
    
    for node in g[src]:
        cur_path.append(node)
        find_all_paths(node, dest, g, cur_path, all_paths)
        cur_path.pop()

def generate_lattice(size):
    lattice = []
    max_node = (size * size) - 1
    
    for i in range(0, max_node):
        if (i % size) == (size - 1):
            lattice.append([i+size])
        elif (i // size) == (size - 1):
            lattice.append([i+1])
        else:
            lattice.append([i+1, i+size])

    lattice.append([])
    
    return lattice        
    
dim = 4
max_node = (dim * dim) - 1
g_lattice = generate_lattice(dim)

cur_path = []
all_paths = []

find_all_paths(0, max_node, g_lattice, cur_path, all_paths)
num_paths = len(all_paths)
print(f'A {dim - 1}x{dim - 1} grid has {num_paths} paths from top right to ' + 
     'bottom left with only right and down moves')


        

    
        
    