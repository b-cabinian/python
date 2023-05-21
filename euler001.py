# -*- coding: utf-8 -*-
"""
Two solutions to Project Euler Problem 1 https://projecteuler.net/problem=1

Author: Brian Cabinian

"""
import time

def sum_multiples_3_5_naive(upper_limt):
    """
    This function computes the sum of all multiples of 3 and 5 less than the
    upper_limit, exclusive.

    Args:
        upper_limt (int): The upper limit of the summation

    Returns:
        sum_val (int): The sum of all multiples of 3 and 5 less than upper_limit

    """
    sum_val = 0
    
    for i in range(0, upper_limit):
        if (i % 3 == 0 or i % 5 == 0):
            sum_val += i
        
    return sum_val

def gauss_sum(n):
    """
    This function returns the sum from 1 to n using Gauss's formula

    Args:
        n (int): the maximum value of the sum

    """
    return (n + 1) * n // 2

def sum_multiples_3_5_gauss(upper_limit):
    """
    This function computes the sum of all multiples of 3 and 5 less than the
    upper_limit, exclusive, using the formula for the sum of the first n

    Args:
        upper_limt (int): The upper limit of the summation

    Returns:
        sum_val (int): The sum of all multiples of 3 and 5 less than upper_limit

    """
    upper_limit_3 = (upper_limit - 1) // 3
    upper_limit_5 = (upper_limit - 1) // 5
    upper_limit_15 = (upper_limit - 1) // 15
    
    sum_val = (3 * gauss_sum(upper_limit_3) + 5 * gauss_sum(upper_limit_5) 
        - 15 * gauss_sum(upper_limit_15))
    
    return sum_val
    

upper_limit = 1000
tic = time.perf_counter()
x = sum_multiples_3_5_naive(upper_limit)
toc = time.perf_counter()
print(f'The naive method returns {x} in {toc - tic:0.6f} seconds')

tic = time.perf_counter()
y = sum_multiples_3_5_gauss(upper_limit)
toc = time.perf_counter()
print(f'Gauss method returns {y} in {toc - tic:0.6f} seconds')

 

