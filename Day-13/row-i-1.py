n=int(input("Enter the size:"))
for i in range(n):
    for sp in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
