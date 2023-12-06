# this is my first prgram

"""
this is my multiline comment  here
 we can write multiple lines
 python wont be consider for exceution
 """

'''
a = 88  # this is  input
b = 5
print(id(a)) #storage 
print(a)

print("sum :" ,a+b)

print("sum of %s and %s is %s" %(a,b,a+b))
                                 
'''
d1={104:'reddy',106:'bhrgav',101:'sharath'}
'''for k in d1.keys():
    print(k)
    '''
'''for v in d1.values():
    print(v)'''
'''for k,v in d1.items():
    print(k,':',v)'''

search=int(input("enter a key:"))
found=True
for k,v in d1.items():
    if (k==search):
        found=True
    if(found==True):
        print("%s is found and the valve is %s"%(search,d1[search]))
