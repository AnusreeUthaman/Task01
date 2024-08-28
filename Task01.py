#Task01

#1-A company decided to give a bonus of 5% to the employee if his/her year of service is more than 5 years.Ask the user for their salary and year of service and print the net bonus amount.
salary= float(input("Enter your salary: "))
yoe= float(input("Enter your experience: "))
if yoe>5:
    print(f"congrats you got a bonus {salary+(salary * (5/100))}")
else:
    print("oops")


#2 Take value of length and breadth of a rectangle from the user and check whether it is square.
l=float(input("Enter the length"))
b=float(input("Enter the breadth"))
if l == b:
    print("Its a square")
    

#03-Take two int values from the user and print the greatest among them
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if a>b:
    print(f"{a} greater than {b}")
elif b>a:
    print(f"{b} greater than {a}")

#04-A shop will give a discount of 10% of the cost of the purchased quantity is more than 1000
#   Ask the user for the quantity
#    suppose ,one unit will cost 100
#    judge and print the total cost for the user

mrp=100
quantity=int(input("Enter the quantity: "))
total=mrp*quantity
if total>1000:
    print("Discounted Total price: {total-(total*(10/100))}")
else:
    print("Total price: {total} ")

#05-A school has the following rules for the grading system:
Below 25-F
25-45-E
45-50-D
50-60-C
60-80-B
above 80-A
#ask the user to enter marks and print the corresponding grade.

score=int(input("Enter your score:"))
if(score<25):
    print("F Grade")
elif(score<45):
    print("E Grade")
elif(score<50):
    print("D Grade")
elif(score<60):
    print("C Grade")
elif(score<80):
    print("B Grade")
else:
    print("A Grade")
print("Thank you")

         
#06-Take input of age of 3 people by the user and determine oldest and youngest among them.
a=10
b=5
c=15
if a>b and a>c:
    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")


#07-Write a python program to check if a number is positive,negative or zero

num=int(input(" Enter a number:"))
if num>0:
    print(num,"is a positive")
elif num<0:
    print(num,"is a negative")
else:
    print(num,"is zero")
'''    

