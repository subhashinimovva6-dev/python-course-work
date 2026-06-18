n = 13
for i in range(n):
    for j in range(n):
        if (i == j and i<=n//2) or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
