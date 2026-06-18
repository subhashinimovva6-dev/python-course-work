n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    if i<m:
        for j in range(i+1):
            print('*',end=' ')
    else:
        for j in range(n-i):
            print('*',end=' ')
    print()
