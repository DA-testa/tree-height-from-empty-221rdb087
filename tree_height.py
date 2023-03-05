# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    heights = [0]*n
    
    for i in range(n):
        if heights[i] !=0:
            continue
    
        height = 0
        while i != -1:
            
            if heights[parents[i]] != 0:
                height += heights[parents[i]]
                break
            height += 1
            i = parents[i]
            
        j = i
        while j != -1:
            if heights[j] != 0:
                break
            heights[j] = height
            height -= 1
            j = parents[j]
    return max(heights)

def main():
   n = int(input().strip())
   parents = list(map(int, input().strip().split()))
   max_height = compute_height(n,parents) 
   print(max_height)


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
