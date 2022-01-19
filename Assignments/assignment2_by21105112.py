print("Program Number 1","\n","\n")


string="Python is a case sensitive language"

print("a part ")
#len function gives the length of the string
print(len(string),"\n")

print("b part")
#[::-1]starting at the end of string and end at position 0
#taking -1 means starting one step backwards
reverse=string[::-1]
print(reverse,"\n")

print("c part")
#string is sliced from 10th to 27th index
sliced=string[10:27]
print(sliced,"\n")

print("d part")
#this variable stores the replace function of string
#replacing sliced variable with "object oriented"
replacewith=string.replace(sliced,"object oriented ")
print(replacewith,"\n")

print("e part")
#This function gives the index number of the input substring
print(string.index("a"),"\n")

print("f part")
#removing white spaces 
strng=string.replace(" ","")
print(strng,"\n")


print("Program Number 2","\n","\n")

name= input("Enter your Name ")
sid_data= input ("Enter your SID ")
department_name= input ("Enter your Department Name ")
cgpa_data=input ("Enter your CGPA ")

#string formatting

name1=" Hey %s Here!"%(name)
sid1="My SID is 2110%s"%(sid_data)
depart1="I am from %s department and my CGPA is %s"%(department_name,cgpa_data)
print(name1,"\n",sid1,"\n",depart1,"\n")

print("Program Number 3","\n","\n")

a=56
b=10
print("a=56","\n","b=10","\n")
# AND operator
print("a & b")

andop=a&b
print(andop,"\n")
# OR operator
print("a | b")

orop=a|b
print(orop,"\n")
# XOR operator
print("a ^ b")

xorop=a^b
print(xorop,"\n")
#Left shift operator 
print("Left shift with 2 bits")

print(a<<2,"\n")

print(b<<2,"\n")
#Right shift operator
print("Right shift of a with 2 bits")

print(a>>2,"\n")

print("Right shift of b with 4 bits")

print(b>>4,"\n")

print("Program Number 4","\n","\n")

num_1= (input("Enter first number "))
num_2= (input("Enter second number "))
num_3= (input("Enter third number "))

if int(num_1) >= int(num_2) and int(num_1) >= int(num_3):
    print((num_1)+" is greatest","\n")
elif int(num_2) >= int(num_1) and int(num_2) >= int(num_3):
    print((num_2)+" is greatest","\n")
else:
    print((num_3)+" is greatest","\n")

print("Program Number 5","\n","\n")

word= str(input("Enter the String "))
# in operator is checking if the given substring is present in the main string 
if ("name") in str(word):
    print("Yes","\n")
else:
    print("No","\n")

print("Program Number 6","\n","\n")

side1=input("Enter the first side ")
side2=input("Enter the second side ")
side3=input("Enter the third side ")

sum1=(side1)+(side2)
sum2=(side2)+(side3)
sum3=(side1)+(side3)

if side1 or side2 or side3 >= sum1:
    print("Yes")
elif side1 or side2 or side3 >= sum2:
    print("Yes")
elif side1 or side2 or side3 >= sum3:
    print("Yes")
else:
    print("No")


