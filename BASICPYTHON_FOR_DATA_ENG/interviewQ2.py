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
def find_avg(ls):
    return float(sum(ls)/len(ls))

ls = [1,2,3,4,5,6]

res = find_avg(ls)
print(res)

# Can a Python function return multiple values? How?
# yes python function will return multiple values in tuple format

# How can you remove duplicates from a list?
ls = [1,2,2,3,4,4,5,1]

def remove_dup(ls):
    new_list = []

    for i in ls:
        if i not in new_list:
            new_list.append(i)

    return new_list

res = remove_dup(ls)
print(res)

# How do you merge two dictionaries in Python?

dict1 = {1 : "one", 2 : "two"}
dict2 = {1 : "onee", 3 : "three", 4 : "four"}

dict3 = dict1  | dict2
print(dict3)

# How can you sort a dictionary by its values?
dict1 = {"five":5,"onee":1, "three":3,"four":4,"two":2}

sorted_dict = dict(sorted(dict1.items(),key= lambda item:item[1]))
print(sorted_dict)


# What is the difference between pop(), remove(), and del in lists?
# pop is used to remove the element with the help of index
# remove is used to remove the element by passing direct value if not found it will rise value error
# del used to remove the all the list at once

ls = [1,2,3,4,5]

print(ls.pop()) # by default it will remove the last value
print(ls.remove(1)) # it will remove the first occurence of the value in the list
print(ls)
del ls
# print(ls)

# How do you count the frequency of each element in a list?

def count_frequence(ls)->dict:

    new_list = dict()

    for value in ls:
        if value not in new_list:
            new_list[value] = 1

        else:
            new_list[value] += 1

    return new_list
 
ls = [1,1,1,2,2,2,3,3,4,5]
res = count_frequence(ls)
print(res)

# What is the difference between a Python module and a package?
# python module is nothing but python file where package is having multipule files in one folder

# How do you import a specific function from a module?
# to import specific function from a module we use (from module name import function name)

# Explain the use of the os and shutil modules in data engineering.
# os and shutil modules are used to do operations with fils structures design

# How would you list all files in a directory using Python?
import os
import glob

path = "/home/ravi/Downloads/Data_eng_workspace/Data_Engineering/BASICPYTHON_FOR_DATA_ENG"

def list_all_files(dir_path):

    if os.path.exists(dir_path):
        files = os.listdir(dir_path)

    return files

res = list_all_files(path)
print(res)
print(os.getcwd())

# What is the purpose of the glob module?
# used to search file with likely patterns
py_files = glob.glob("*.txt")
print(py_files)

# How would you read a CSV file without using Pandas?
