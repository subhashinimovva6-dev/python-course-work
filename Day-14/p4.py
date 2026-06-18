n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    if i<=m:
        print(' '*(m-i)+'*'*(i+1),end=' ')
    else:
        print(' '*(i-m)+'*'*(n-i),end=' ')
    print()
        
