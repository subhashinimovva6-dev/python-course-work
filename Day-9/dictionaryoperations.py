Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d['demo']='str'
d
{1: 'int', 12.3: 'float', 'demo': 'str'}
d[2+3j]='complex'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d[False]='bool'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex', False: 'bool'}
d={}
d[1]=1
d
{1: 1}
d[23]=23.4
d[3]='fghj'
d[4]=3+4j
d[5]=[1,2,3]
d[6]=(1,2,3)
d[7]={1,3}
d[8]={1:1,2:2}
d[9]=False
d
{1: 1, 23: 23.4, 3: 'fghj', 4: (3+4j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3}, 8: {1: 1, 2: 2}, 9: False}
d={}
d
{}
d[1]=14
d
{1: 14}
d={}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1:2,2:4,3:6,4:8,5:10,6:12}
d[4]
8
d[6]
12
d[1]
2
d[4]
8
d={'komalatha':89,'bhargavi':76,'subha':90,'harika':89,'maha':65}
d
{'komalatha': 89, 'bhargavi': 76, 'subha': 90, 'harika': 89, 'maha': 65}
d['subha']
90
d['harika']
89
d.get('gaya')
d.get('maha')
65
d.get('akhil','user not found')
'user not found'
d.get('subha','user not found')
90
d
{'komalatha': 89, 'bhargavi': 76, 'subha': 90, 'harika': 89, 'maha': 65}
'subha' in d
True
'harika' in d
True
'maha' not in d
False
d.keys()
dict_keys(['komalatha', 'bhargavi', 'subha', 'harika', 'maha'])
d.values()
dict_values([89, 76, 90, 89, 65])
d.items()
dict_items([('komalatha', 89), ('bhargavi', 76), ('subha', 90), ('harika', 89), ('maha', 65)])
sorted(d)
['bhargavi', 'harika', 'komalatha', 'maha', 'subha']
max(d)
'subha'
min(d)
'bhargavi'
len(d)
5
d
{'komalatha': 89, 'bhargavi': 76, 'subha': 90, 'harika': 89, 'maha': 65}
d['dinesh']
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    d['dinesh']
KeyError: 'dinesh'
d['maha']
65
d['maha']=100
d
{'komalatha': 89, 'bhargavi': 76, 'subha': 90, 'harika': 89, 'maha': 100}
d['komalatha']=95
d
{'komalatha': 95, 'bhargavi': 76, 'subha': 90, 'harika': 89, 'maha': 100}
d['subha']=99
>>> d
{'komalatha': 95, 'bhargavi': 76, 'subha': 99, 'harika': 89, 'maha': 100}
>>> d.update({'gaya':87,'sam':67})
>>> d
{'komalatha': 95, 'bhargavi': 76, 'subha': 99, 'harika': 89, 'maha': 100, 'gaya': 87, 'sam': 67}
>>> d.popitem()
('sam', 67)
>>> d
{'komalatha': 95, 'bhargavi': 76, 'subha': 99, 'harika': 89, 'maha': 100, 'gaya': 87}
>>> d.popitem()
('gaya', 87)
>>> d
{'komalatha': 95, 'bhargavi': 76, 'subha': 99, 'harika': 89, 'maha': 100}
>>> d.pop('maha')
100
>>> d
{'komalatha': 95, 'bhargavi': 76, 'subha': 99, 'harika': 89}
>>> del d['komalatha']
>>> d
{'bhargavi': 76, 'subha': 99, 'harika': 89}
>>> d.clear()
>>> d.setdefault('harika',0)
0
>>> d
{'harika': 0}
>>> d.setdeafault('rishi',45)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    d.setdeafault('rishi',45)
AttributeError: 'dict' object has no attribute 'setdeafault'. Did you mean: 'setdefault'?
>>> d
{'harika': 0}
>>> d={'komalatha': 95, 'bhargavi': 76, 'subha': 99, 'harika': 89, 'maha': 100}
>>> d
{'komalatha': 95, 'bhargavi': 76, 'subha': 99, 'harika': 89, 'maha': 100}
>>> d.setdefault('harika',0)
89
>>> d
{'komalatha': 95, 'bhargavi': 76, 'subha': 99, 'harika': 89, 'maha': 100}
