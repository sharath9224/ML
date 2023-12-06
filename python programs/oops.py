# class
'''
class sample:
    def myfun1(self):
        print('hi everyone')
    def myfun2(self):
        print("hello everyone")
#program excecution starts here
obj1=sample()
print(type(obj1))
obj1.myfun1()
obj2=sample()
obj1.myfun1()
obj1.myfun2()
obj2.myfun1()
obj2.myfun2()
'''
'''
class student:
    def inputmarks(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def add(self):
        print(self.m1+self.m2)
#program exceution starts here
sarath=student()
bhargav=student()
sarath.inputmarks(84,91)
bhargav.inputmarks(81,87)
sarath.add()
bhargav.add()

'''

#constructor
'''
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def change(self,m2):
        self.m2=m2
    def add(self):
        print(self.m1+self.m2)
sarath=student(87,85)
bhargav=student(88,86)
sarath.add()
bhargav.add()
sarath.change(99)
sarath.add()
bhargav.add()
'''
'''
class employee:
    def __init__(self,eno,ename,sal):
        self.eno=eno
        self.ename=ename
        self.sal=sal
    def hike(self,sal):
        self.sal=sal
        
    def display(self):
        print("Eno :",self.eno,end="/t")
        print("Ename :",self.ename,end="/t")
        print("Sal:",self.sal)
        
    
sarath=employee(105,"reddy",65000)
bhargav=employee(102,"kumar",65525)
sarath.display()
bhargav.display()
sarath.hike(95000)
bhargav.hike(96000)
print("after hike in salary ")
sarath.display()
bhargav.display()

'''

#instance and class variable
'''
class cars:
    wheels=4  #class variable
    def __init__(self,company,milage):  #init method
        self.company =company
        self.milage = milage   #instance variable
    def output(self):
        print("Company:",self.company,end="\t")
        print("Milage:",self.milage,end="\t")
        print("Wheels:",self.wheels,end="\t")  #or we can cars.wheels
c1=cars("kia",20) #object declaration
c2=cars("bmw",25)
c1.output()
c2.output()
#c1.milage=30 #changing the instance variable
cars.wheels=5 # changing the class variable
c1.output()
c2.output()
'''

#inner class
'''
class outer:
    def __init__(self,ov):
        self.ov=ov
        self.in1=self.inner(88)
    class inner:
        def __init__(self,iv):
            self.iv =iv
obj1 =outer(5)
#obj2 =inner(55)
print("outer class",obj1.ov)
print("inner class",obj1.in1.iv)
  '''

#inheritance

#single inheritance
'''
class parent:
    def function1(self):
        print("this is function1 of parent")
class child(parent):
    def function2(self):
        print("this is function2 of child")
c1=child()
c1.function1()
c1.function2()

p1 =parent()
p1.function1()
p1.function2()
'''

#Multi level inheritance
'''
class GParent:
    def function1(self):
        print("this functin of grand parent class")
class Parent:
    def function2(self):
        print("this is function of parent class")
class Child:
    def function3(self):
        print("this is function of child class")
c1 = Child()
c1.function1()
c1.function2()
c1.function3()
'''

#multiple inheritance
'''
class parent1:
    def function1(self):
        print("this is function1 in parent")
class parent2:
    def function2(self):
        print("this is function2 in parent2")
class child(parent1,parent2):
    def function3(self):
        print("this is function3 in child class")
c1 =child()
c1.function1()
c1.function2()
c1.function3()
    '''
#hierarchical inheritance
'''
class parent:
    def function1(self):
        print("this is function1 in class parent")
class child1(parent):
    def function2(self):
        print("this is function2 in class child")
class child2(parent):
    def function3(self):
        print("this is function3 in child class2")
c1= child1()
c1.function1()
c1.function2()

c2 =child2()
c2.function1()
c2.function3()
'''
'''
class Addition:
    def add(self,a,b):
        print(a+b)
class subtraction:
    def subtract(self,a,b):
        print(a-b)
class Multiplication:
    def multiple(self,a,b):
        print(a*b)
class division:
    def divide(self,a,b):
        print(a/b)
class Mathfunctions(Addition,subtraction,Multiplication,division):
    def moddivide(self,a,b):
        print(a%b)
class addsub(Addition,subtraction):
    pass
c1 = Mathfunctions()
c1.add(2,3)
c1.subtract(7,4)
c1.multiple(3,3)
c1.divide(9,2)
c1.moddivide(15,2)
c2=addsub()
'''
'''
#single inheritance in super init

class parent:
    def __init__(self):
        print("this is parent init")
    def function1(self):
        print("parent class -this is function1")
class child(parent):
    def __init__(self):
        super().__init__()
        print("this is child init")
    def function2(self):
        print("child class-this is functin2")
c1=child()
c1.function1()
c1.function2()
'''

#multiple inheritance in super init
'''
class parent1:
    def __init__(self):
        print("this is parent1 init")
        super().__init__()
    def function1(self):
        print("this is function1")
class parent2:
    def __init__(self):
        print("this is parent2 init")
    def function2(self):
        print("this is parent2 class")
class child(parent1,parent2):
    def __init__(self):
        super().__init__()
        print("this is child class")
    def function3(self):
        print("this is function3")
c1 = child()
c1.function1()
c1.function2()
c1.function3()
 '''

#polymorphism
#operator over loading
'''
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1 +other.m1
        m2=self.m2 +other.m2
        s3=student(m1,m2)
        return s3
    def output(self):
        print(self.m1)
        print(self.m2)
s1=student(87,56)
s2=student(65,85)
s3=s1+s2
s3.output()
'''
#method over loading
'''
class sample:
    def add(self,a,b=None,c=None):

        if(a!=None and b!=None and c!=None):
            s=a+b+c
        elif(a!=None and b!=None):
            s=a+b
        else:
            s=a
        return s
s1.sample()
print(s1.add(2,3,4))
print(s1.add(2,3))
print(s1.add(2))
'''

#method over riding
'''
class parent:
    def output(self):
        print("this is parent class")
class child(parent):
        def output(self):
            print("this is child output")
obj1=child()
obj1.output()
'''

#duck typing
class car:
    def fuel(self):
        print("car runs with petrol")
        print("car runs with diesel")
class Bike:
    def fuel(self):
        print("bike runs with petrol")
class Ebike:
    def fuel(self):
        print("ebike runs with electricity")
for obj in car(),Bike(),Ebike():
    print("data tpe of an object:",type(obj))
    obj.fuel()
