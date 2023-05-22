# -*- coding: utf-8 -*-
"""
Author: Brian Cabinian
Description: Fast solution to Project Euler Problem 15. Given the movement 
constraint, the lattice can be broken up into two perfect binary trees 
along the right diagonal. The number of paths to a leaf of one of the trees 
is given by the binomial coefficient C(n, k) where n is the leaf level of the
tree and k is it's entry position. So the number of paths from the 
root1 -> leafx and leafx -> root2 is C(n, k)^2. 

https://projecteuler.net/problem=15
"""
import math
import unittest

# Int -> Int
# Purpose: Take a grid dimension and calculate all the ways you can traverse
# from the upper left to the lower right only moving down or right
def lattice_path_count(dim):
    coeffs = generate_binomial_coefficients(dim)
    
    return square_and_sum(coeffs)

# List of Int -> Int
# Purpose: Take a list, square all it's entries, then sum it
def square_and_sum(coefficients):
    return sum(map(lambda n : n * n, coefficients))

# Int -> List of Int
# Purpose: returns all the binomial coefficients in a given row, n, of Pascal's
# triangle. Rows of the triangle are 0 indexed
def generate_binomial_coefficients(n):
    pascal_triangle = [[1], [1, 1]]
    
    if (n > 1):
        for row in range(1, n):
            pascal_triangle.append(next_row(pascal_triangle[row]))
    
    return pascal_triangle[n]
    

# List of Int -> List of Int
# Purpose: Given upper row of binomial coefficient, return next row
def next_row(current_row):
    next_row = []
    n = len(current_row)
    next_ceil_halfway = math.ceil((n + 1) / 2)
    next_floor_halfway = math.floor((n + 1) / 2)
    
    for entry in range(0, next_ceil_halfway):
        if entry == 0:
            next_row.append(1)
        else:
            next_row.append(current_row[entry - 1] + current_row[entry])
    
    for entry2 in range(next_floor_halfway - 1, -1, -1):
        next_row.append(next_row[entry2])
    
    return next_row
        
          
# Unit tests for functions above
class TestProblem15Functions(unittest.TestCase):

    def test_next_row(self):
        self.assertEqual(next_row([1, 1]), [1, 2, 1])
        self.assertEqual(next_row([1, 2, 1]), [1, 3, 3, 1])

    def test_generate_binomial(self):
        self.assertEqual(generate_binomial_coefficients(0), [1])
        self.assertEqual(generate_binomial_coefficients(2), [1, 2, 1])
        self.assertEqual(generate_binomial_coefficients(3), [1, 3, 3, 1])
        
    def test_square_and_sum(self):
        self.assertEqual(square_and_sum([0, 0]), 0)
        self.assertEqual(square_and_sum([3, 3]), 18)
        self.assertEqual(square_and_sum([2, 5, 2]), 33)
        
    def test_lattice_path_count(self):
        self.assertEqual(lattice_path_count(2), 6)
        self.assertEqual(lattice_path_count(3), 20)
        self.assertEqual(lattice_path_count(4), 70)

if __name__ == '__main__':
    unittest.main()


num_paths = lattice_path_count(20)
print(f'A 20x20 grid has {num_paths} paths from top right to ' + 
     'bottom left with only right and down moves')

    
        
    