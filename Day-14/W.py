n = int(input("Enter n: "))

for i in range(n):
    for j in range(2 * n - 1):
        if j == 0 or j == 2 * n - 2 or \
           (i >= n // 2 and j == i) or \
           (i >= n // 2 and j == (2 * n - 2 - i)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
