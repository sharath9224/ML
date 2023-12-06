'''def sample(): #function definaation
    #print("im reddy")
    print("from washington ")
#program excutes here 
print("im gajjala")
sample() #function call
print("welcome to sonic solutions'''

'''
def add(a,b):  #function def and a,b are called arguments/parameters
    print("add :",a+b)
    print("diff:", a-b)
    print("prod:",a*b)
    print ("div:",a/b)
x=int(input("enter X:"))
y=int(input("enter Y:"))
add(x,y)
print("done")
    
'''
'''

def area_of_circle(r):
    area=(22/7)*r*r
    print("area of a circle:",area)

re=float(input("enter a radius:"))
area_of_circle(re)

'''
'''
def add(a,b):
    return(a+b)
x=int(input("enter x valve:"))
y=int(input("enter y valve:"))
s=add(x,y)
print("sum:",s)
'''

#with args and with return type
'''
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return(f)
#program excution starts here
n= int(input("enter a number:"))
f=fact(n)
print("factorial:",f)

#with args and with out return type

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print("factorial:",f)
n= int(input("enter a vlave:"))
fact(n)
print("next")
'''

#without arg and with return type
'''def fact():
    n=int(input("enter a valve:"))
    f=1
    for i in range(1,n+1):
        f=f*i
    return(f)
f=fact()
print("factorial:",f)'''


#with out args and  without return type
'''
def fact():
    n=int(input("enter a vlave:"))
    f=1
    for i in range(1,n+1):
        f=f*i
    print("factorial:",f)
fact()
print("next statement ")
  '''
#nested function
'''
def display():  #function def
    print("this is display function")
    def show():   #function def
        print("this is show function")
    show()#function call
display() #function call
'''

#passing any type of arguments
'''def display(a,b):
    print(a+b)
display(24,25)
display(25.36,66.32)
display("anand","kumar")
display([14,25,36,52,63],[66,35,58,96,75])
'''

#passing function as parameter
'''def display(sh):
    print("this is display function"+sh())
def show():
    return("this is show")
display(show)    
'''

#passing function as a parameter and return the function from function to main program
'''def display(sh):
    print("this is display function")
    return (sh)
def show():
    print("this is  show function")
r_sh=display(show)
print(r_sh())
'''

#local variable
'''def sample1():
    a=87
    print("valve of sample1:",a)
def sample2():
     print("valve of sample2",a)
#program exceution starts here
sample1()
#sample2()
print("valve of main :",a)
'''
#global variable
'''def sample1():
    print("valve of a in sample1:",a)
def sample2():
    print("valve of sample2:",a)
a=99
sample1()
sample2()
print("main valve")
  '''
#positional arguments - the number of actual and formal should be same these should be in same order

'''def add(a,b,c):
    print(a+b+c)
#program exceution starts here
add(22,52,10,20)
'''
#default arguments 
'''def sample(eno,ename,sal=50000):
    print("ENO:",eno)
    print("ENAME:",ename)
    print("SAL:",sal)
sample(102,"raji",5589363.33)
sample(103,"siva")
'''
'''def add(a,b=0,c=0,d=0):
    print(a+b+c+d)
add(11,10,21,33)
add(22,12,66)
add(10,11)
add(11)
'''
#variable length arguments
'''def sample(*args):
    s=0
    for i in args:
        s=s+i
    print("sum:",s)
sample(55,20,15,41,36,88,22)
sample(22,66,96)'''


'''def sample(custid,name,*args):
    print("Cust Id:",custid,end="\t")
    print("Name:",name,end="\t")
    s=0
    for i in args:
        s=s+i
    print("sum:",s)
sample(105,"reddy",55,20,15,41,36,88,22)
sample(102,"jaier",22,66,96)'''
 #keyword variable length arguments
'''def sample(**kwargs):
    for k,v in kwargs.items():
        print(k,":",v)
sample(one=111,two=222,three=333,four=444)
sample(fname="reddy",mname="kumar",lname="vennapusa")'''

# A function can call another function
'''def display():
    print("this is display function")
    show()
def show():
    print("this is show function")
#program exceution starts here
display()'''

#recursion -- a function called by itself
def fact(n):
    if(n==0):
        return(1)
    return(n*fact(n-1))
n= int(input("enter num:"))
f =fact(n)
print("factorial:" ,f)
