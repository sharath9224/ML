''' sum of first n natural numbers 
n =int(input("enter a number:"))
s=0
for i in range(1,n+1):
    s=s+1
print("sum :",s)
'''

#print even numbers with in range
'''n1=int(input("enter N1:"))
n2=int(input("enter N2:"))
for i in range(n1,n2+1):
    if(i%2==0):
        print(i)
'''


#print sum of even and odd numbers with in a range
'''
n1 =int(input("enter n1:"))
n2 =int(input("enter n2:"))
se=0
so=0
for n in range(n1,n2+1):
    if(n%2==0):
        se=se+n
    else:
        so=so+n
print("sum of even:",se)
print("sum of odd :",so)
'''

#print sum of odd and even  numbers in a list
'''
list1 =[15,75,94,82,77,91,58,67,22,34]
se=0
so=0
for i in list1:
    if(i%2==0):
        se=se+i
    else:
        so=so+i
print("sum:",se)
print("sum:",so)
'''

'''
n= int(input("enter N1:"))
f=0
for i in range(1,n):
    if(n*i==0):
        
        print(i)
 '''    

'''
n = int(input("enter :"))
f =0
for i in range(1,n+1):
    if(n%i==0):
        f=f+1
if(f==2):
    print("%S",n)
    '''

'''

n = int(input("enter :"))
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+1
if(s==n):
    print("%s is a perfect number" %n)
else:
    print("%s is not a perfect number" %n)
    '''
'''
for i in range(1,5):
    for j in range(1,5):
        print(i,end="")
    print()
'''
'''
for i in range(1,5):
    for j in range(1,5):
        print(j,end="")
    print()
    '''
'''
for i in range(1,5):
    for j in range(1,5):
        print("*" ,end="")
    print()
    '''

'''
for i in range(1,5):
    for j in range(1,i+1):
        print(i,end="")
    print()
    '''
'''
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()
    '''
'''
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()
    '''
'''
#prime numbers with in a range
n1= int(input("enter n1:"))
n2=int(input("enter n2:"))
for n in range(n1,n2+1):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        print(n)
        '''

#for loop with else
for i in range(1,10):
    print(i)
else:
    print("else part")
