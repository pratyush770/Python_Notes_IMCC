# There are 3 rods and are stacked from large to small
def towerOfHanoi(n, A, B, C):
    if n == 1:
        print(f"Move disk from {A} to {C}")
        return
    towerOfHanoi(n-1, A, C, B)  # recursive call
    towerOfHanoi(1, A, B, C)
    towerOfHanoi(n - 1, B, A, C)


# calling program
n = 3
towerOfHanoi(n, 'A', 'B', 'C')
