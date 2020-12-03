# program using zip() function and list() function, create a merged list of tuples from the two lists given
l1=[1,2,3,4,5,6]
l2=[7,8,9,10,11,12]
a=zip(l1,l2)
print(tuple(a))

# create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.
num=range(1,8)
l3=[1,2,3,4,5,6,7]
b=zip(num,l3)
print(tuple(b))

# Using sorted() function, sort the list in ascending order.
l4=[80,10,4,1,78,39,90,45,100]
sort=sorted(l4)
print(sort)

# program using filter function, filter the even numbers so that only odd numbers are passed to the new list.
l5=[1,2,3,4,5,6,7,8,9,10,11,12]
newlt=list(filter(lambda x:(x%2!=0),l5))
print(newlt)

