#vowels:
s='looping statements'
for i in s:
    if i in 'aeioouAEIOU':
        print(i)


#even or odd:
l=[56,76,32,3,34,2,3,5,97,45,23,98,76,32]
for i in l:
    if i%2==0:
        print(i)

#dict:
d={'laptops':0,'chargers':2,'keyboards':10,'tab':0,'mouse':5}
for i in d:
    if d[i]:
        print(i)

#tuple:
t=(9,2,13,4,5,6)
for i in range(len(t)):
    print(i*t[i])

#converts to uppercase:
names={'subha','harika','maha','gaya','sandy'}
for i in names:
    print(i.upper())
