Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s1={55,69,78,53,86,99}
s2={55,66,5,3,53,99,72}
print(s1)
{99, 69, 53, 86, 55, 78}
print(s2)
{66, 3, 99, 5, 53, 55, 72}
print(s1|s2)
{66, 99, 3, 69, 5, 72, 78, 53, 86, 55}
print(s1.intersectin(s2))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(s1.intersectin(s2))
AttributeError: 'set' object has no attribute 'intersectin'. Did you mean: 'intersection'?
print(s1.intersection(s2))
{99, 53, 55}
print(s1&s2)
{99, 53, 55}
print(s1.union(s2))
{66, 99, 3, 69, 5, 72, 78, 53, 86, 55}
print(s1.intersection_update(s2))
None
print(s1)
{99, 53, 55}
s1={55,69,78,53,86,99}
print(s2.intersection_update(s2))
None
print(s2)
{66, 3, 99, 5, 53, 55, 72}
print(s2.intersection_update(s1))
None
print(s2)
{99, 53, 55}
print(s1-s2)
{78, 69, 86}
print(s2-s1)
set()
s3={55,69,5,3,53,99}
print(s1>s2)
True
print(s1>s3)
False


fs=frozenset([5,24,36,96,49,55])
print(type(fs))
<class 'frozenset'>
fs=frozenset([5,24,36,96,49,55,55,24,5,99,32])
print(fs)
frozenset({96, 32, 99, 36, 5, 49, 55, 24})
fs=frozenset

#dictionary
d1={104:'reddy',106:'bhrgav',101:'sharath'}
print(type(d1))
<class 'dict'>
print(d1)
{104: 'reddy', 106: 'bhrgav', 101: 'sharath'}
d1[101]
'sharath'
d1[105]='kumar'
print(d1)
{104: 'reddy', 106: 'bhrgav', 101: 'sharath', 105: 'kumar'}
d1[106]='vennapusa'
print(d1)
{104: 'reddy', 106: 'vennapusa', 101: 'sharath', 105: 'kumar'}
d1[102]='reddy'
print(d1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
print(d1)
{104: 'reddy', 106: 'vennapusa', 101: 'sharath', 105: 'kumar', 102: 'reddy'}
del d1[104]
print(d1)
{106: 'vennapusa', 101: 'sharath', 105: 'kumar', 102: 'reddy'}
d1.keys()
dict_keys([106, 101, 105, 102])
d1.values()
dict_values(['vennapusa', 'sharath', 'kumar', 'reddy'])
d1.items()
dict_items([(106, 'vennapusa'), (101, 'sharath'), (105, 'kumar'), (102, 'reddy')])

= RESTART: C:\Users\Sharath Reddy\OneDrive\Desktop\sharath\python programs\sample1.py
104
106
101

= RESTART: C:\Users\Sharath Reddy\OneDrive\Desktop\sharath\python programs\sample1.py
reddy
bhrgav
sharath

= RESTART: C:\Users\Sharath Reddy\OneDrive\Desktop\sharath\python programs\sample1.py
Traceback (most recent call last):
  File "C:\Users\Sharath Reddy\OneDrive\Desktop\sharath\python programs\sample1.py", line 26, in <module>
    for k,v in d1.keys():
TypeError: cannot unpack non-iterable int object
>>> 
= RESTART: C:\Users\Sharath Reddy\OneDrive\Desktop\sharath\python programs\sample1.py
104 : reddy
106 : bhrgav
101 : sharath
>>> 
= RESTART: C:\Users\Sharath Reddy\OneDrive\Desktop\sharath\python programs\sample1.py
enter a key:101d1={104:'reddy',106:'bhrgav',101:'sharath'}
Traceback (most recent call last):
  File "C:\Users\Sharath Reddy\OneDrive\Desktop\sharath\python programs\sample1.py", line 29, in <module>
    search=int(input("enter a key:"))
ValueError: invalid literal for int() with base 10: "101d1={104:'reddy',106:'bhrgav',101:'sharath'}"
>>> 
= RESTART: C:\Users\Sharath Reddy\OneDrive\Desktop\sharath\python programs\sample1.py
enter a key:101
Traceback (most recent call last):
  File "C:\Users\Sharath Reddy\OneDrive\Desktop\sharath\python programs\sample1.py", line 35, in <module>
    print("%s is found and the valve is %S"%(search,d1[search]))
ValueError: unsupported format character 'S' (0x53) at index 30
>>> 
= RESTART: C:\Users\Sharath Reddy\OneDrive\Desktop\sharath\python programs\sample1.py
enter a key:101
101 is found and the valve is sharath
101 is found and the valve is sharath
101 is found and the valve is sharath
