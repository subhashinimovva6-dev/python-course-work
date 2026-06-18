n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if  i == 0 or (i==4 and j<3) or (i==3 and j==0) or (i==2 and j==0) or j==n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
