# What are Python’s mutable and immutable data types? Give examples.
""" mutable data types : {dict,sets,list}
immutable data types : {int,float,string,complex,tuple}"""

# What’s the difference between a list, tuple, and set in Python?
# list --> ordered , mutable , duplicates are allowed
# tuple --> ordered , immutable , duplicates are allowed
# sets --> unordered , mutable , duplicates are not allowed

ls = [1,2,3,4,5]

# operations on list ( add element,delete element,modify element)
# adding element
ls.append(6)

# delete element
ls.remove(5) # this will remove the first occurence value if value not present it will through an error

# modify element
ls[0] = 10 # modifying the value in first index

# what is pop in the python
ls.pop() # it will remove the value by thier index , it will rise index out of range error.

# sets 
s = {1,2,3,4,5}

# operations in sets (add,remove)
s.update({6,7,5})
print(s)

# How do you swap the values of two variables without using a third variable?
a,b = 5,10
print(a,b)
a,b = b,a
print(a,b)

# What’s the difference between shallow copy and deep copy in Python?   
# shallow copy will only copys outer object
import copy

ls = [[1,2],[3,4]]

a = copy.copy(ls)
print(a)

a[0][1] = 10
print(a,ls)

ls1 = [[1,2],[3,4]]

b = copy.deepcopy(ls1)
print(b)

b[0][1] = 10
print(b,ls1)

ls = [1,2,3,4,5]
print(ls,type(ls))

ls1 = tuple(ls)
print(ls1,type(ls1))


# Write a Python program to print all even numbers from 1 to 50.

def call_even(input)->list:
    result = []
    for i in range(1,input + 1):
        if i % 2 == 0:
            result.append(i)

    return result

even_value = call_even(50)
print(even_value)

# How can you iterate over both index and value of a list at the same time?
ls = [1,2,3,4,5]

length = len(ls)

for i in range(length):
    print(f'index : {i} , value {ls[i]}')

# Write a loop to print the Fibonacci sequence up to 100.

def fibonacci_sequence(num : int)->list:

    a,b = 0,1
    result = []
    while a <= num:
        result.append(a)

        a,b = b,a + b

    return result

res = fibonacci_sequence(100)
print(res)






