'''a = int(input("enter:"))
if (a>=90 and a<=100):
    print("A grade")
elif(a>80 and a<90):
    print("B grade")
elif(a>70 and a<80):
    print("c grade")
elif (a>60 and a<70):
    print("D grade")
elif(a>0 and a<60):
    print("fail")
else:
    print("not eligiable")
'''

'''
a = int(input("enter A marks :"))
if (a==1):
    print("one")
elif (a==2):
    print("two")
elif(a==3):
    print("three")
elif(a==4):
    print("four")
elif(a==5):
    print("five")
else:
    print("invalid")'''


'''username=input("enter username:")
if (username=="reddy"):
    print("correct")
    pw=(int(input("enter a password :")))
    if(pw==re1234):
                 print("correct")
    else:
        print("incorrect")
else:
    print("incorrect username")'''



'''uname=input("enter username:")
pw=int(input("enter password:"))
if (uname=="reddy" and pw=="1234"):
    print("correct") 
else:
    print("incorrect username and/or password")

'''


'''list1 = [55,85,25,32,96]
s=0
for i in list1:
    s=s+1
print("sum:", s)'''


list1 =[54,37,12,68,96,83,29]
'''s=0
for i in list1:
    s=s+i
print("sum :",s)
print("sum:",sum(list1))'''

'''
search=int(input("enter:"))
if (search in list1):
    print("%s is found" %search)
else:
    print("%s is not found" %search)
'''

''''
search=int(input("enter:"))
found= False
for i in list1:
    if(i==search):
        found =True
if(found==True):
    print("%s is found" %search)
else:
    print("%s is not found" %search)
search=(int(input("enter a num:")))
if(search in list1):
    print("%s is found" %search)
else:
    print("%s is not found" %search)'''


'''
name="shararh reddy"
print('length of string:',len(name))
c=0
for i in name:
    c=c+1
print('length of string:' ,c)'''


n = int(input("enter a number:"))
for i in range(10,n+1):
    print(i)

        
