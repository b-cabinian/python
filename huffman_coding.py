# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 19:18:54 2021

Author: Brian Cabinian
Description: Given a frequency dictionary, this script creates a Huffman tree. 
This script was written as a demonstration for a SRJC CS4 Discrete Math class.
"""

class Node:
    def __init__(self, key, val, left, right):
        self.key = key
        self.val = val
        self.left = left
        self.right = right        

def generate_huff_tree(freq_dict):
    #create list of nodes
    forest = [Node(k, v, False, False) for k, v in freq_dict.items()]
    
    while len(forest) != 1:
        #sort nodes by frequency
        new_forest = sorted(forest, key = lambda node: node.val)
    
        #combine two smallest trees
        n1 = new_forest[0] 
        n2 = new_forest[1]
        
        #n2 is larger and it becomes left branch
        x = Node(n1.key + n2.key, n1.val + n2.val, n2, n1)
        
        forest = new_forest[2:]
        forest.insert(0, x)
        
    return forest[0]

def get_huff_code(key, node):
    code = ''
    while key != node.key:
        if key in node.left.key:
            #add 0 for left fork
            code = code + '0'
            node = node.left
            
        elif key in node.right.key:
            #add 1 for right fork
            code = code + '1'
            node = node.right
           
        else:
            raise ValueError('key not found in tree')
            
    return code


freq_dict = {'h': 0.12,
             'm': 0.16, 
             'a': 0.19, 
             's': 0.24, 
             't': 0.29}

x = generate_huff_tree(freq_dict)