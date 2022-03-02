print("1","\n")

print(" Solution the problem of tower of Hanoi with three disks: ")

def hanoi(n, first, second, third):
    if n == 0:
        return
    
    hanoi(n-1, first, third, second)
    print(f"Move Disk {n} from {first} to {second}")
    hanoi(n-1, third, second, first)
    
#calling funtion for 3 disks
hanoi(3, 'A', 'B','C')
print("\n")
      
print("2","\n")

rows=int(input("Enter the number of rows in Pascal's Triangle: "))

def pascal(rows, somerows=rows):
    if rows == 0:
        return
    
    pascal(rows-1,somerows)
    print('  '*(somerows-rows), end='')
    entry =1
    
    for i in range(1, rows+1):
        print(entry, end ='   ')
        entry = entry*(rows - i) // i
    print()
pascal(rows)

print("\n")

for line in range(1, rows+1):
    print('  '*(rows- line), end='')
    x = 1
    for i in range(1, line+1):
        print(x, end='   ')
        x = x * (line - i) // i
    print()
print("")
print("\n")

print("3","\n")

a=int(input("Enter the first integer: "))
b=int(input("Enter the first integer: "))
c=a%b
d=a//b
print("Remainder is: ", c)
print("Quotient is: ",d)
print("\n")

print("a","\n")
      
c1=callable(divmod(c,d))
if c1==True:
    print("Function is callable")
if c1==False:
    print("Function is Not-callable")
print("\n")

print("b","\n")

if(c!=0):
    if (d!=0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")
print("\n")

print("c","\n")

thislist=[c,d]
for i in range (4,7):
    thislist.append(i)
print(f"Added (4,5,6) in the values ({c},{d})")
newlist=[]
#adding number greater than 4 from thislist to newlist
for i in thislist:
    if i>4:
        newlist.append(i)
#a new list listfinal with same elements as newlist but in string form
listfinal=list(map(str,newlist))
#Using join
element=",".join(listfinal)
print(f"Values greater than 4 are {element}")
print("\n")

print("d","\n")

set1={1,2}
set1.clear()
#adding above result in set datatype
for data in newlist:
    set1.add(data)
print("Above result in set form is shown below:")
print(set1)
print("\n")

print("e","\n")

print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("\n")

print("f","\n")

print("Largest value in the set: ", max(set2))
mega=max(set2)
print("Hash value: ", hash(mega))
print("\n")

print("4","\n")

class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid

    def __del__(self):
        print("Object destroyed")

#creating object
student1 = Student("Tarush", 21105112)
print("Object created")

print(f"The name of the student is {student1.name} and their SID is {student1.sid}.")

#deleting object
del student1
print("\n")

print("5","\n")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __del__(self):
        print(f"The record of Employee {self.name} is deleted")

#creating new employees database
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#updating the salary
print("a part")
employee1.salary = 70000
print(f"The updated salary of the employee {employee1.name} is {employee1.salary}")

#deletion of a record
print("b part")
print(" ", end='')
del employee3
print("\n")

print("6","\n")

#inputting a word from the first friend
word = input("Enter the first word: ")
print("\n")
#inputting a meaningful word with the exact same letters
testword = input("Enter a new meaningful word to test your friendship: ")

#defining dictionary from last assignment
def count_in_dict(word):
    count = {}
    listin = list(word)
    n = len(listin)
    
    for i in range(n):
        if listin[i] in count:
            count[listin[i]] += 1
        else:
            count[listin[i]] = 1
    return count

#test to verify the letters of the new word
if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact,your friendship is fake")
else:
    #code for the shopkeeper, to check if the word makes sense or not
    def userinput():
        shop = input("Does the word makes sense?(yes or no) ")
        print("\n")
        
        if shop == 'yes':
            print("The friends passed the friendship test")
            print("\n")

        elif shop == 'no':
            print("The word doesn't have a meaning,your friendship is fake")
            print("\n")

        else:
            print("Invalid input, try again")
            userinput()
    userinput()



    
   



