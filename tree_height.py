import sys
import threading

def compute_height(n, parents):
    children = {i: [] for i in range(n)}
    
    for i, parent in enumerate(parents):
        if parent != -1:
            children[parent].append(i)
    def calc_height(node):
        if not children[node]:
            return 1
        else:
            return 1 + max([calc_height(child) for child in children[node]])
        
    max_height = 0
    for i in range(n):
        height = calc_height(i)
        if height > max_height:
            max_height = height
    return max_height

def main():
    # read input
    source = input()
    if source == "I":
        n = int(input())
        parents = list(map(int, input().split()))
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

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

threading.Thread(target=main).start()
