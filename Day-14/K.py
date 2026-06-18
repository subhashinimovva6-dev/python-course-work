'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if j==0 or (j==4 and i==0) or (j==3 and i==1) or (j==4 and i==4) or (i==2 and j<3) or (i==3 and j==3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
n = 13
for i in range(n):
    for j in range(n):
        if j==0 or (i==j and i>n//2) or (i+j==n-1 and i<n//2)or (i==n//2 and j<=n//2):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
