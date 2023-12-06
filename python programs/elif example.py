'''a = int(input("enter A:"))
b = int(input("enter B:"))
c = int(input("enter C:"))
if (a>b and a>c):
    print("%s is bigger than %s and %s" %(a,b,c))
elif(b>c):
    print("%s is bigger than %s and %s "%(b,a,c))
else:
    print("%s is bigger than %s and %s " %(c,a,b))
        
'''

r = float(input("enter a valve:"))
a =3.14*r*r
if (a<100):
     print("smaller circle")

elif(a>100 and a<200):
    print("medium circle")
else :
    print("large circle")
