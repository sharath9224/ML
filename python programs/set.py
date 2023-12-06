Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1={25,63,96,23,55,63,84,52,98}
>>> print(s1)
{96, 98, 52, 23, 84, 55, 25, 63}

>>> print(len(s1))
8
>>> s1.add(68)
>>> print(s1)
{96, 98, 68, 52, 23, 84, 55, 25, 63}
>>> s1.update([66,55,87,63,96,41])
>>> print(s1)
{96, 98, 66, 68, 41, 52, 23, 84, 55, 87, 25, 63}
>>> s1.pop()
96
>>> print(s1)
{98, 66, 68, 41, 52, 23, 84, 55, 87, 25, 63}
>>> s1.remove(68)
>>> print(s1)
{98, 66, 41, 52, 23, 84, 55, 87, 25, 63}
>>> s1.remove(65)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s1.remove(65)
KeyError: 65
>>> s1.discard(65)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.discard(65)
NameError: name 's' is not defined. Did you mean: 's1'?
>>> s1.discard(65)
>>> s1.clear()
>>> print(s1)
set()
>>> print(type(s1))
<class 'set'>
