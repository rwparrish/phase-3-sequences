#!/usr/bin/env python3
import ipdb
 
 
def print_fibonacci(length):
    fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    i = 0
    if length == 0:
        print('', end="")
    while length > 0:
        print(fib_sequence[i])
        i += 1
        length -= 1
        
    
    
    
    
    
        
