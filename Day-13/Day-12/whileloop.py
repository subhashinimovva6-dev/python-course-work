'''
int
while condition
update
statement
'''
i=1
while i<11:
    print(i)
    i+=1


#even:
i=2
while i<21:
    print(i)
    i+=2

#10-1:
i=10
while i>0:
    print(i)
    i-=1

#iteration-5:
i=5
while i<51:
    print(i)
    i+=5

#iteration of loop:
l=[1,2,3,4,5,6,9,8]
i=0
while i<len(l):
    print(l[i])
    i+=1

#iteration of string:
s='python programming'
i=0
while i<len(l):
    print(l[i])
    i+=1


#iteration of tuple:
l=(1,2,3,4,5,6,9,8)
i=0
while i<len(l):
    print(l[i])
    i+=1

#removing zeros from the list:
l=[1,0,0,2,3,4,0,0,0,0,2,0,0,1,0,3,50,2,0,64,23,0,0,0,0,0,12,3,34]
while 0 in l:
    l.remove(0)
print(l)

#candycrush game:
moves=30
while moves>1:
    status = input("[w]in or [c]ontinue").upper()
    if status=='w':
        print("you won the game")
        break
    moves-=1
    print(f'{moves} moves are left')
else:
    print("game over")
