print("1","\n")

string=input("")
count=len(string.split())
words=string.split()
counts=dict()
#if the input has more than one word
if count!=1:
    
    def wordcounter(string):
        for string in words:
            if string in counts:
                #couting each word
                counts[string]+=1
            else:
                counts[string]=1
        return counts
    print(wordcounter(string),"\n")
#if the input has single word    
elif count==1:
    
    def charcounter(string):
        for i in range(len(string)):
            if len(string)==0:
                break
            #counting each character
            char=string[0]
            if char=='' or char=='\n':
                continue
            print(char+" ",string.count(char))
            string=string.replace(char,'').strip()
    print(charcounter(string))
print("\n")

print("2","\n")


day_input=int(input("Enter the date "))

if day_input>31:
     print("Invalid")
else:
     month_input=int(input("Enter the month "))
     
     if month_input>12:
          print("Invalid")
     else:
          year_input=int(input("Enter the year "))
          
          if year_input>=2050:
               print("Limit Exceeded")
          elif year_input<=1800:
               print("Limit Exceeded")
          else:
              #to check if its leap year or not
               if (year_input % 400 ==0):
                    leap_year = True
               elif (year_input % 100 ==0):
                    leap_year = False
               elif (year_input %4 ==0):
                    leap_year = True
               else:
                    leap_year = False
               #storing all the months with 31 days 
               bigmonths=[1,3,5,7,8,10,12]
               
               if month_input in bigmonths:
                    month_length = 31
               elif month_input == 2:
                    if leap_year:
                         month_length = 29
                    else:
                         month_length = 28
               else:
                    month_length = 30          
               #incrementing day_input     
               if day_input <month_length:
                    day_input += 1
               else:
                    day_input = 1
                    #incrementing year_input
                    if month_input == 12:
                         month_input = 1
                         year_input += 1
                    else:
                        #incrementing month_input
                         month_input+= 1

               print("The next date is %s %s %s"%(day_input, month_input, year_input))
               print("\n")

print("3","\n")

inputlist=[5,22,45,67,100]
#taking square of every element in the list by for loop
result=[(element,pow(element,2)) for element in inputlist]
print(result)
print("\n")

print("4","\n")

result=int(input("Enter your grade "))

if result==(10):
    print("Your Grade is 'A+' and Outstanding Performance")
elif result==(9):
    print("Your Grade is 'A' and Excellent Performance")
elif result==(8):
    print("Your Grade is 'B+' and Very Good Performance")
elif result==(7):
    print("Your Grade is 'B' and Good Performance")
elif result==6:
    print("Your Grade is 'C+' and Average Performance")
elif result==(5):
    print("Your Grade is 'C' and Below Average Performance")
elif result==(4):
    print("Your Grade is 'D' and Poor Performance")
else:
    print("Grade Entered: Out of range")
print("\n")

print("5","\n")

string="ABCDEFGHIJK"
#formation of letters
listforstring=[]
for i in string:
    listforstring.append(i)
k=1
while k<=6:
    #for printing the row
    for element in listforstring:
        print(element,end="")
    #for printing second row
    #using pop function to remove last letter
    listforstring.pop(len(listforstring)-1)
    listforstring.pop(len(listforstring)-1)
    listforstring.insert(0," ")
    print()
    k=k+1
print("\n")

print("6","\n")

dic={}
dic2={}
repeat="Y"
ynlist=["Y","y","N","n"]

while repeat=="Y" or repeat=="y":
    name_input=str(input("Enter the student Name "))
    sid_input=int(input("Enter the student Sid "))
    if sid_input<0:
        print("Error")
    else:
        #updating the dic and dic2
        dic.update({sid_input:name_input})
        dic2.update({name_input:sid_input})
        repeat=str(input("Enter Y to continue "))
    if repeat=="N" or repeat=="n":
        break
    elif(not(repeat in ynlist)):
        print("error")
        repeat=str(input("Enter Y to continue "))
        print("\n")

print("a part","\n")
#printing the dictionary
print(dic,"\n")

print("b part","\n")
#printing sorted dictionary with accordance to name
newlist=sorted(dic2)
dic3={}
for element in newlist:
    dic3.update({element:dic2.get(element)})
print(dic3,"\n")

print("c part","\n")
#printing sorted dictionary with accordance to sid
sortedlist=sorted(dic)
dic4={}
for element in sortedlist:
    dic4.update({element:dic.get(element)})
print(dic4,"\n")

print("d part","\n")
#finding the name with its key name
sid_name=int(input("Enter SID to get name "))
output=str(dic.get(sid_name))
print({sid_name},(output))
print("\n")


print("7","\n")

nterms=int(input("Enter a positive number "))
nstring=str(input)

if nterms<=0:
    nterms=int(input("Enter a positive number "))
else:
    n1,n2=0,1
    count=0
#fibonacci series loop
while count<nterms:
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1
    print(n2)
    list007=[n2]
sum=0
#printing average of the resultant series
for number in list007:
    some=sum+number
    avg=(some//nterms)
print("And its average is ",avg)
print("\n")



print("8","\n")

Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

print("a.","\n")
'''
set1-set2 U set2-set1
'''
both=Set1.difference(Set2)
both2=Set2.difference(Set1)
both3=both.union(both2)
print(both3)
print("\n")

print("b.","\n")
'''
[set1 U set2] U set3
[set1 ⊓ set2]
[set2 ⊓ set3]
[set1 ⊓ set3]
then [set1 U set2] U set3 - [set1 ⊓ set2] - [set2 ⊓ set3] - [set1 ⊓ set3]
'''
notunique=Set1.union(Set2)
notseparate=notunique.union(Set3)
unique=Set1.intersection(Set2)
common=Set2.intersection(Set3)
separate=Set1.intersection(Set3)
subtract=notseparate-unique-common-separate
print(subtract)
print("\n")

print("c.","\n")
'''
([set1 ⊓ set2] U [set2 ⊓ set3]) U [set1 U set3] - ([set1 ⊓ set2] ⊓ set3)
'''
unique=Set1.intersection(Set2)

common=Set2.intersection(Set3)

separate=Set1.intersection(Set3)

bigunion=unique.union(common)
megaunion=bigunion.union(separate)

divider=unique.intersection(Set3)
minus=megaunion-divider
print(minus)
print("\n")

print("d.","\n")
'''
[{1,..10}^set1]
[{1,..10}^set1] - {1,..10}
'''
unique={1,2,3,4,5,6,7,8,9,10}
common=Set1
squal=unique.symmetric_difference(common)
print(squal)
print("\n")

print("e.","\n")
'''
[{1,..10}^set1 and set2 and set3]
{1,..10} - [{1,..10}^set1 and set2 and set3]
'''
unique={1,2,3,4,5,6,7,8,9,10}
common=Set1 and Set2 and Set3
squal=unique.symmetric_difference(common)
ss=unique.difference(squal)
print(ss)
print("\n")






