'''
rows = 5

for i in range(rows):
    for j in range(rows * 2 - 1):
        if j == i or j == (rows * 2 - 2 - i):
            print("*", end="")
        else:
            print(" ", end="")
    print()
'''
n = 15
for i in range(n):
    for j in range(n):
        if (i==j and j<=n//2)or (i+j==n-1 and j>n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
