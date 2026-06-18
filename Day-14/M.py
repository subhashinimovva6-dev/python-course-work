n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==2 and j==2) or (i==1 and j==1) or (i==1 and j==3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
