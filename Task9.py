#lambda fn that multiply argument x with argument y
a=lambda x,y:x*y
print(a(4,2))

#fibonacci series to n
def fib(n):
    b=[0,1]
    any(map(lambda _:b.append(b[-1]+b[-2]),range(2,n)))
    print(b)
n=int(input("Number"))
fib(n)

#multiply each number of list with a no
l=list(range(20))
l=list(map(lambda n:n*5,l))
print(l)

#nos divisible by 9
l=list(range(100))
l1=list(filter(lambda n:(n%9==0),l))
print(l1)

#count the even nos in the list
l=list(range(1,20))
count=len(list(filter(lambda n:(n%2==0) ,l)))
print(count)