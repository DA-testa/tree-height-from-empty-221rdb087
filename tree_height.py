# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    children = {}    
    for i in range(n):
        children[i] = []
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            children[parent].append(i)
    def calc_height(node):
        if not children[node]:
            return 0
        else:
            return 1+max([calc_height(child) for child in children[node]])
    return calc_height(root)
        

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
