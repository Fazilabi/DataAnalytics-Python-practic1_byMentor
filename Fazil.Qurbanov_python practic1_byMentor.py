#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
# task 1
num = int(input("enter number :"))

if num>0:
    while num>=1:
        num/=5
        print(num)
        if num==1:            
            break
        else: continue
    if num==1:
        print("is power")
    else: print("not power")
    
else:print("enter positive number")

# ***********************************************************************


# task 2
number  = int(input("enter number :"))
cube_root = round(number**(1/3))
cube  = cube_root**3
if cube==number:
    print("yes")
else:print("no")

# ***********************************************************************

# task 3
number = int(input("enter number :"))
tax = 1
if number<0:
    print("number must be positive")
elif number<500:
    print("no tax - number is :", number)
elif number<1000:
    number*=0.1
    print(number)
else: 
    number*=0.15
    print(number) 

# ***********************************************************************
    
#task 4

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
diff=0
if num1<num2:
    diff=num2-num1
    print(num2 , " is bigger than ", num1, "difference is ", diff)
elif num2<num1:
    diff=num1-num2
    print(num1, " is bigger than ", num2,"difference is ", diff)
else:
    print("numbers is equal")
# ***********************************************************************
    
# task 5

number  = int(input("enter number :"))
div=1;
if number == 1:
    print("1 is neither simple or complex")
elif number==2:
    print("prime")
else:
    for x in range(number):
        if number%(x+2)==0:
            print("complex")            
        else: print("prime")
        break
        
# ***********************************************************************
        
# task 6

number  = int(input("enter number :"))
count = 0
while number>10:
    if number%3==0:
        count+=1
    number/=3
print(count)

# ***********************************************************************

# task 7

list1 = [12,5,7,6,4,10]
#print(list[1:-1])
#print(list[0],list[-1])
#print(list2)
#print(list3)    


list3=list1[1:-1]

list2=[]
list2.append(list1[0])
list2.append(list1[-1])

sum1 = 0;
sum2 = 0;
for i in list2:
    sum1+=i
print(sum1)
for j in list3:
    sum2+=j
print(sum2)
if sum1>sum2:
    print("sum of first and last items of list is greater than others.")
elif sum1<sum2:
    print("sum of first and last items of list is smaller than others.")
else: print("sum of firts and last otems of list is equal with others.")

# ***********************************************************************


# task 8
num = int(input("enter number :"))
if num%100==0:
    if num%400==0:
        print(num ," is leap year1")
    else: print(num ," is not leap year1")
elif num%4==0:
        print(num ," is leap year2")
else: print (num , " is not leap year3")

# ***********************************************************************

# task 9
num=int(input("Enter number:"))
count=0
while(num>0):
    count=count+1
    num=num//10
print("The number of digits in the number are:",count)

# ***********************************************************************

# task 10
side1 = float (input("enter first side of triangle: "))
side2 = float (input("enter second side of triangle: "))
side3 = float (input("enter third side of triangle: "))
if (side1+side2)>side3 and (side2+side3)>side1 and (side1+side3)>side2:
    print("possible")
else: print("not possible")

# ***********************************************************************






"""



