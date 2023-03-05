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
    source = input()
    if source == "I":
        n = int(input())
        parents = list(map(int, input().strip().split()))
    elif source == "F":
        file_name = input().strip()
        if "a" in file_name:
            sys.exit()
        try:
            with open(file_name, "r") as file:
                n = int(file.readline().strip())
                parents = list(map(int, file.readline().strip().split()))
        except FileNotFoundError:
            sys.exit()
    else:
        sys.exit()
        
    max_height = compute_height(n, parents)
    print(max_height)

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
