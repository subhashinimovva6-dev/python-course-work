n=int(input("Enter the size:"))
c=1
for row in range(n):
    for col in range(row+1):
        print(str(c).zfill(3),end=' ')
        c+=1
    print()
    
