# print n- numbers
'''n= int(input("enter:"))
i=1
while(i<=n):
    print(i)
    i=i+1
    '''
#print sum of n-numbers
'''
n = int(input("Enter :"))
s=0
i=1
while(i<=n):
    s=s+1
    i=i+1
print("Sum :",s)
'''
'''
n = int(input('enter :'))
i=10
while(i<=1):
    print('%s X %s =%s' %(i,n,i*n))
    
    i=i+1'''
 # palindrome number
'''
st=input("enter a string:")
if(st==st[::-1]):
   print("%s is palindromr string" %st)
else:
    print("%s is not palindrome string" %st)
'''

#strong number
n= int(input("enter:"))
temp=n
s=0
while(n>0):
    d=n%10
    f=1
    for i in range(1,d+1):
        f=f*i
    s=s+f
    n=n//10
if(s==temp):
    print("%s is a strong numer" %temp)
else:
    print("%s is n0t a strong number" %temp)
