#File Handling

# How do you read a text file line by line in Python?
path = "/home/ravi/Downloads/Data_eng_workspace/Data_Engineering/BASICPYTHON_FOR_DATA_ENG/All_Questions_only.txt"
with open(path,'r') as f:
    data = f.readlines()

print(data)

# What’s the difference between read(), readline(), and readlines()?
# read() --> read all the content in the file 
# readline --> it will read the first line in the file
# readlines --> it will return all lines in list format

# How can you write a dictionary into a JSON file?
import json

data = {
    "emp1":{'name':'raghu','dept':'bigboss','salary':70000},
    "emp2":{'name':'gilli','dept':'bigboss','salary':80000}
}

with open('data.json', 'w') as f:
    json.dump(data,f,indent=4)

# Explain the use of the with open() statement in file handling.
# in file handling with open statment used for it will auto-metically ensure that file closed safly

# Write a Python script to count the number of lines in a file.
def count_lines(file_path):

    line_count = 0
    with open(file_path,'r') as f:
        # data = f.readlines()
        for line in f:
            line_count += 1

    return line_count

res = count_lines(path)
print(res)

# Functions

# How do you define a function in Python?
# using def key word we can define a function

# What are default arguments, *args, and **kwargs?
# default arguments are used if caller don't provide it

# example
# def greet(user = "user!"):
#     print(f'Hello , {user}')

# greet()
# greet('Ravi')

def greet(age,user = 'user!'):
    print(f'Hello,{user} and you are {age} old')

greet(25)
greet(25,'Ravi')

# Write a function that takes a list of numbers and returns their average.
