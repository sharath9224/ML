#zero divisionerror: division by zero
'''
x=12
y=0
print(x/y)
print("end of program")
'''
'''
x=12
y=0
try:
    print(x/y)
except Exception:
    print("you can't divide by zero")
print("end of program")
'''


#exception error
'''
x=12
y=0
try:
    print(x/y)
except Exception as ex:
    print("you can't divide by zero",ex)
print("end of program")
'''
#final exception

x=12
y=0
try:
    print("logic open")
    print(x/y)
except Exception as ex:
    print("you can't divide as zero",ex)
else:
    print("this is logic error")
finally:
          print("logic close")
print("end of program")

#file handling read,write
#read
'''
fr=open("file1r.txt","r") #mode --read
#print(fr.read()) #prints entire file 
#data=fr.read()
#print(data)
#print(fr.readline()) #prints first line
#print(fr.read(15)) #prints the characters
'''

#write
'''
fw=open("file2.txt","w")
fw.write("now u have complete the task in 2 days\n")
fw.write("ur selected when u will join\n")
fw.close()
'''


#create the specified file ,returns the errr if it exists
'''
f=open("file3.txt","x")
f.write("now u have go for hr round \n")
f.write("salary discussions")
f.close()
'''

#Appending a file
'''
f=open("file2.txt","a")  #append
f.write("\n due to covid hirings are less \n")
f.write("now it is better to sustain")
f.close()
'''
#file concepts using functions
'''
def fileread():
    f=open("file1r.txt","r")
    print(f.read())
def fileappend():
    f=open("file1r.txt","a")
    f.write("\n this is good one to select\n")
    f.write("we can go now")
    f.close()
print("program exceution strts here")
fileread()
fileappend()
print("**** appending the data*******")
fileread()
'''

#iterators
'''
list1 =[15,55,88,69,36,20]
it1=iter(list1)
print(it1.__next__())
print(it1.__next__())
print(it1.__next__(),it1.__next__(),it1.__next__())
for i in it1:
    print(i.__ne__())
'''