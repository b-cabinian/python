# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 13:31:42 2021

Author: Brian Cabinian
Description: Given an indexed list of cities and an associated adjacency
matrix, this script uses the dijkstra algorithm to find the shortest 
path between any two cities. This script was written as a demonstration for
a SRJC CS4 Discrete Math class.

"""

import numpy as np

def dijkstra_path_find(start, end, nodes, adj_matrix):
    """
    Find the shortest path between two nodes in a given graph of cities with 
    edges representing flight prices between cities.

    Args:
        start (string): The starting node
        end (string): The ending node
        nodes (dict): nodes of the graph, dict keys are node labels referring 
        to cities, dict values are for indexing adjacency matrix
        adj_matrix (numpy array): adjacency matrix of graph, representing 
        flight prices between cities

    Returns:
        shortest_path_weight (float): The total weight of the shortest path.
        final_path (list): A list of the nodes from the start to the end node 
        with the shortest path

    """
    
    #keeps track of the lowest weight path to a given city
    city_path = {c : np.inf for c in nodes.keys()}
    #keeps track of the shortest path 
    short_path = {c : "" for c in nodes.keys()} 
    city_path[start] = 0
    
    visited_nodes = set()
  
    while end not in visited_nodes:
        #find all cities not checked
        cities = set(city_index.keys())
        unvisited_nodes = cities - visited_nodes
        
        #recast as list because you have to index into the list later
        unvisited_list = list(unvisited_nodes)
        
        #get path lengths associated with each unvisited city 
        #and find min path length
        unvisited_path_lengths = [city_path[c] for c in unvisited_list]
        min_path_length = min(unvisited_path_lengths)
        u = unvisited_path_lengths.index(min_path_length)
        
        min_city = unvisited_list[u]
        visited_nodes.add(min_city)
        
        #check if the path length from start city through current min_city to 
        #unvisited city < the current known shortest path length from start to 
        #unvisited city
        for i in unvisited_nodes:
            new_path = city_path[min_city] + adj_matrix[city_index[min_city], city_index[i]]
            if new_path < city_path[i]:
                city_path[i] = new_path
                short_path[i] = min_city
    
    shortest_path_weight = city_path[end]
    final_path = rec_short_path(end, start, short_path)
    
    #alternatively, using lisp-like recursion:
    # final_path = list(iter_cons(lisp_rec_short_path(end, start, short_path)))
    # final_path.reverse()
    
    return (shortest_path_weight, final_path)

def rec_short_path(end, start, short_path_dict, shortest_path = []):
    """
    unwrap shortest path from short_path_dict in dijkstra algorithm
    
    Args:
        end (String): The end node
        start (String): The start node
        shortest_path_dict (dict): a dict generated from the dijkstra algorithm
        shortest_path (list): by default an empty list, which develops into a 
        list of the shortest path between start and end
    
    Returns:
        shortest_path(list): A list of the nodes from the start to the end node 
        with the shortest path
    """
    if end == start: 
        shortest_path.append(end)
        shortest_path.reverse()
        return shortest_path
    else:
        shortest_path.append(end)
        return rec_short_path(short_path_dict[end], start, short_path_dict, shortest_path)

def lisp_rec_short_path(end, start, short_path_dict):
    """
    unwrap shortest path from short_path_dict 
    
    Args:
        end (String): The end node
        start (String): The start node
        shortest_path_dict (dict): a dict generated from the dijkstra algorithm
    
    Returns:
        LISP like tuple of tuples that contains the reversed shortest path 
    """
    if end == start: 
        return (end, None)
    else:
        return (end, rec_short_path(short_path_dict[end], start, short_path_dict))

def iter_cons(seq):
    """
    convert LISP-like constructed tuple of tuples to generator object, which 
    can be recast as a list
    """
    while seq is not None:
        car, cdr = seq
        yield car
        seq = cdr


"""=============INPUT==============="""
city_index = {"Boston": 0 ,
              "New York": 1,
              "Miami": 2,
              "Atlanta": 3,
              "Chicago": 4,
              "Denver": 5,
              "San Francisco": 6,
              "Los Angeles": 7}

adj_matrix = np.array([[0, 39, 0, 0, 79, 0, 0, 0],
                       [39, 0, 99, 79, 59, 0, 129, 129],
                       [0, 99, 0, 69, 0, 0, 0, 0],
                       [0, 79, 69, 0, 99, 0, 0, 0],
                       [79, 59, 0, 99, 0, 69, 99, 0],
                       [0, 0, 0, 0, 69, 0, 89, 89],
                       [0, 129, 0, 0, 99, 89, 0, 39],
                       [0, 129, 0, 0, 0, 89, 39, 0]])

#convert all 0's to infinity for ease of data input
adj_matrix = np.where(adj_matrix == 0, np.inf, adj_matrix)

start = "San Francisco"
end = "Boston"
y = dijkstra_path_find(start, end, city_index, adj_matrix)

print(y[0])
print(y[1])