# List down all the error types - using python program

##Syntax error

if 2<3
  print("True")

##Division by zero error

try:
  print(5/0)
except ZeroDivisionError:
  print("Division by zero error")

##Key error

try:
  a={'hema':'19','deepa':'20'}
  a['shine']
except KeyError:
  print("Key not found error")

##Module not found error
try:
  import module1
except ModuleNotFoundError:
  print("Module not found")


#calculator
def calc():
         try:
           n1=int(input("Number 1 : "))
           n2=int(input("Number 2 : "))
           result=input("Operation: +,-,*,/")
           if result=='+':
             print(" Add:",n1+n2)
           elif result=='-':
            print(" Subtract:",n1-n2)
           elif result=='*':
            print(" Multiply:",n1*n2)
           elif result=='/':
             try:
              print(" Division:",n1/n2)
             except ZeroDivisionError:
               print("division by zero error")
         except ValueError:
           print("enter valid input")
calc()


#Print one message if the try block raises a NameError and another for other errors
try:
  print(name)
except NameError:
  print("Name is not defined")
except:
  print("Other error has occured")


#Input inside the try catch block
try:
  name1=int(input("Enter your name"))
  print(name1)
except:
  print("An exception occurs")
