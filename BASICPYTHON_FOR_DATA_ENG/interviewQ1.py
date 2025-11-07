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