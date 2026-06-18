n=int(input("Enter the size:"))
for i in range(n):
    for sp in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()
