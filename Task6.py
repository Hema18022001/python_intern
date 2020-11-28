# loop through list of nos
x = list(range(0, 20))
print(f"List is {x}")
x = [i + 2 for i in x]
print(f"Updated list:{x}")


#pattern
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

#fibonacci series
a,b,s=0,1,0
n=int(input("Enter the no of terms"))
for i in range(i,n+1):
    print(s,end=" ")
    a=b
    b=s
    s=a+b

#Armstrong number
n=input("Enter the number")
n1=list(n)
no=int(n)
n2=[int(int(i)) for i in n1]
l=len(n2)
n3=[pow(i,l) for i in n2]
if sum(n3) == no:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")

# Multiplication table of 9
i = 9
for j in range(1, 20):
    print(f"{i}*{j}={i * j}")

# To check whether a no. is positive or negative
n = int(input("Number:"))
if n > 0:
    print("Positive")
else:
    print("Negative")

# days to ages
day = int(input("Enter no of days"))
print(f"The age is:{day // 365}")

# trigonometry using math functions
import math
h = math.sin(90) * 2 + math.cos(90) * 2
print(f"(sin90)^2+(cos90)^2={h}")

# Simple calculator
k = int(input("Number 1 : "))
l = int(input("Number 2 : "))
m = input("Select the operator : +,-,*,/")
if m == '+':
    print(f"{k}+{l}={k + l}")
elif m == '-':
    print(f"{k}-{l}={k - l}")
elif m == '*':
    print(f"{k}*{l}={k * l}")
elif m == '/':
    print(f"{k}/{l}={k / l}")
