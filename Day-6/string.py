Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python programming'
len(s)
18
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
min(s)
' '
max(s)
'y'
ord('a')
97
ord('A')
65
ord('o')
111
ord(' ')
32
chr(98)
'b'
chr(120)
'x'
chr(30)
'\x1e'
chr(35)
'#'
chr(37)
'%'
s='python programming'
s.upper()
'PYTHON PROGRAMMING'
s.lower()
'python programming'
s.capitalize()
'Python programming'
s.title()
'Python Programming'
s.swapcase()
'PYTHON PROGRAMMING'
s.casefold()
'python programming'
'%'
'%'
#alignment methods
s
'python programming'
s.center(28,'-')
'-----python programming-----'
s.ljust(28,'-')
'python programming----------'
s.rjust(28,'-')
'----------python programming'
'123'.zfill(5)
'00123'
'123'.zfill(10)
'0000000123'
'123'.zfill(3)
'123'
'123'.zfill(2)
'123'
#search & find methods
s
'python programming'
s.find('g')
10
s.rfind('o')
9
s.find('z')
-1
s.index('o')
4
s.rindex('o')
9
s.count('y')
1
s.count('m')
2
#replace & modify methods
s
'python programming'
s.replace('python','java')
'java programming'
s.maketrans('python','123456')
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.translate(s.maketrans('python',123456'))
                        
SyntaxError: unterminated string literal (detected at line 1)
s.translate(s.maketrans('python','123456'))
                        
'123456 1r5grammi6g'
#splittin&joining methods
                        
s='java,python,javascript,c,c++'
                        
s.split(',')
                        
['java', 'python', 'javascript', 'c', 'c++']
s.split(',',2)
                        
['java', 'python', 'javascript,c,c++']
s.rsplit(',',2)
                        
['java,python,javascript', 'c', 'c++']
g='sdfgh'
                        
g='''dsfghjk'''
                        
>>> g='''dfghjk
... fghjkl;
... gfhjkl
... drtyuhj'''
...                         
>>> g
...                         
'dfghjk\nfghjkl;\ngfhjkl\ndrtyuhj'
>>> s.splitlines()
...                         
['java,python,javascript,c,c++']
>>> g.splitlines()
...                         
['dfghjk', 'fghjkl;', 'gfhjkl', 'drtyuhj']
>>> l=['java,python,javascript', 'c', 'c++']
...                         
>>> ''.join(l)
...                         
'java,python,javascriptcc++'
>>> '-'.join(l)
...                         
'java,python,javascript-c-c++'
>>> '@'.join(l)
...                         
'java,python,javascript@c@c++'
>>> ' '.join(l)
...                         
'java,python,javascript c c++'
>>> #partition methods
...                         
>>> s
...                         
'java,python,javascript,c,c++'
>>> s.partition(',')
...                         
('java', ',', 'python,javascript,c,c++')
>>> s.rpartition(',')
...                         
('java,python,javascript,c', ',', 'c++')
