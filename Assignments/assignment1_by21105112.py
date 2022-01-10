print("\n"+"Program Number 1")

from math import *
num1= input("Enter the first number: ")
num2=input("Enter the second number: ")
num3=input("Enter the third number: ")

sum= float(num1)+float(num2)+float(num3)
avg= sum//3
print("Your Average is "+str(avg))


print("\n"+"Program Number 2")


gross_income= input("Enter your gross income ")
no_of_dependents= input("Enter the amount of dependents ")
standard_deduction= (10000)
dependent_deduction= (3000)

taxing=float(gross_income)-float(standard_deduction)

tax_income=(taxing)-(int(no_of_dependents)*float(dependent_deduction))

tax=float(tax_income)*20//100


print("Your income tax is","\n",(tax))

print("\n"+"Program Number 3")


print("student = [(SID),(Name),(Gender),(CourseName),(CGPA)]")
#storing diiferent values 
Student_data=[2133,'Tarush','M','Computing',6.7]
print("Student data = ",Student_data)


print("\n"+"Program Number 4")

#unsorted list
Marks= [67,83,78,57,89]
print("Marks of 5 students "+"\n"+str(Marks))
#sorted list
Marks.sort()
print("Marks in sorted manner "+"\n"+str(Marks))

print("\n"+"Program Number 5")

print("a_part")

color= ["Red","Green","White","Black","Pink","Yellow"]
#To remove a particular element from the list
color.pop(3)

print(color)

print("b_part") 


color= ["Red","Green","White","Black","Pink","Yellow"]
#to remove and add a particular element in the list
color[3:5]=["Purple"]

print(color)
