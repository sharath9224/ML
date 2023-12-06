#generators
'''
def sample():
    yield(25,66,75)
    yield(25,"reddy",558.36)
    yield 22
    yield 69
val =sample()
print(val.__next__())
print(val.__next__())
print(val.__next__())
print(val.__next__())
'''
'''
#topten  squares
def topten():
    n=1
    while n <= 10:
        yield n*n
        n=n+1
valves=topten()
for i in valves:
    print(i)
 '''

#decators
#method 1 : without changing the function
'''
def div(a,b):
    print(a/b)
a=int(input("enter a :"))
b=int(input("enter b:"))
if (a>b):
    div(a,b)
else:
    a,b =b,a
    div(a,b)
'''
#Method 2: with changing the function
'''
def div(a,b):
    if a<b:
        a,b =b,a
    print(a/b)
a=int(input("enter A:"))
b=int(input("enter B:"))
div(a,b)
'''

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b =b,a
        return func(a,b)
    return inner
@smart_div
def div(a,b):
    print(a/b)
a=int(input("enter A:"))
b=int(input("enter B:"))
div(a,b)
    
