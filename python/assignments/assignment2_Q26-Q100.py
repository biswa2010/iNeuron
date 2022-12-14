#Q26. What is a string? How can we declare string in Python?

'''
strings are a collection of characters surrounded by quotes. And strings are immutable in python.

string_name = "string_value"
string_name2 = str("1002")
'''

#Q27. How can we access the string using its index?

'''
strVariableName[<index>]
'''

# Q28. Write a code to get the desired output of the following
'''
string = "Big Data iNeuron"
desired_output = "iNeuron"
'''

string = "Big Data iNeuron"
desired_output = string[9:]

print(desired_output)

#Q29. Write a code to get the desired output of the following
'''
string = "Big Data iNeuron"
desired_output = "norueNi"
'''
'''
string = "Big Data iNeuron"
desired_output = string[-1:-8:-1]

print(desired_output)
'''
#Q30. Resverse the string given in the above question.

'''
string = "Big Data iNeuron"
'''
string = "Big Data iNeuron"
desired_output = string[-1::-1]

print(desired_output)

#Q31. How can you delete entire string at once?

str1 = "hello"
del str1

#Q32. What is escape sequence?

'''
escape sequence are used to use some escape characters using "\" by which interpreter doesn't interprete it as a special character and its considered as a string literal.
'''

#Q33. How can you print the below string?
'''
'iNeuron's Big Data Course'
'''
string = "'iNeuron\'s Big Data Course'"
print(string)

#Q34. What is a list in Python?

'''
List is a data structure in python which are used to store multiple items in a single variable. 
There is no restrictions that it can store a same type of values
'''

#Q35. How can you create a list in Python?

list_1 = []
list_2 = [1,2, "hello", (1,2)]

#Q36. How can we access the elements in a list?
'''
Elements of list can be accessed via its index (list_name[i]).
'''

#Q37. Write a code to access the word "iNeuron" from the given list.
'''
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
''' 
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
print(lst[4][2])

#Q38. Take a list as an input from the user and find the length of the list.

size = int(input("Enter the list size:"))

print("Enter the list elements:")
lst = []
for i in range(0,size):
    num = int(input())
    lst.append(num)
print(lst)


#Q39. Add the word "Big" in the 3rd index of the given list.
'''
lst = ["Welcome", "to", "Data", "course"]
'''
lst = ["Welcome", "to", "Data", "course"]

lst.insert(2, "Big")
print(lst)

#Q40. What is a tuple? How is it different from list?

'''
Tuple is similar to list but it is defined using "()" and it is IMMUTABLE.
'''

#Q41. How can you create a tuple in Python?

tuple = () # Empty tupple
tuple_2 = ("hello", 1, true)
tuple_3 = ("single element tuple",) # for single element needs to add comma else its a string


#Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.
'''
No not able to add, as its immutable in nature.
'''

#Q43. Can two tuple be appended. If yes, write a code for it. If not, why?

'''
No two tuples can't be appended, as its immutable.
But yes we can create another tuple with appended values
'''

#Q44. Take a tuple as an input and print the count of elements in it.

input = tuple(input("Enter space separated tuple values").split(" "))

print(len(input))

#Q45. What are sets in Python?
'''
Sets are a collection which contains unique values and these are unordered and unindexed.
'''

#Q46. How can you create a set?

set_1 = set()
set_2 = {1,2,"hello"}

#Q47. Create a set and add "iNeuron" in your set.

set_value = set()
set_value.add("iNeuron")


#Q48. Try to add multiple values using add() function.

#Q49. How is update() different from add()?

#Q50. What is clear() in sets?
'''
clear() in sets used to clear all the elements available in that set and the set becomes an empty set.
'''

#Q51. What is frozen set?

'''
frozenset in an immutable set which can be created by passing iterable object. And it stores unique elements like sets.
'''

#Q52. How is frozen set different from set?
'''
frozensets are immutable unlike set and frozenset can only be created by passing iterable object(we can't create it by passing any non iterable object/variable). 
'''

#Q53. What is union() in sets? Explain via code.
a = {1,2,3}
b = {4,5,6,6}
c = a | b
print(c)

#Q54. What is intersection() in sets? Explain via code.
a = {1,2,3,4,6}
b = {4,5,6,6}
c = a & b

print(c)

#Q55. What is dictionary in Python?
'''
Its a key value pair where keys are unique where keys can be either an integer or a string and values can be anything
'''
#Q56. How is dictionary different from all other data structures.

#Q57. How can we delare a dictionary in Python?

dict_1 = {}
dict_2 = {5:6, "hello":5, 10:[1,2,3]}


#Q58. What will the output of the following?
'''
var = {}
print(type(var))
'''
'''
<class 'dict'>
'''

#Q59. How can we add an element in a dictionary?

dict_1 = {1:"hello","A":1}
dict_1[3] = 5
print(dict_1)

#Q60. Create a dictionary and access all the values in that dictionary.

dict_1 = {1:"hello","A":1}
dict_1[3] = 5
print(dict_1)

for values in dict_1.values():
    print(values)

#Q61. Create a nested dictionary and access all the element in the inner dictionary.

dict_1 = {1:"hello","A":1,"numbers":{5:"five",6:"six"}}

for elems in dict_1["numbers"].items():
    print(elems)

#Q62. What is the use of get() function?

'''
get(<key_name>) is used to get the corresponding value
'''

#Q63. What is the use of items() function?

'''
items() is used for getting all the elements(key-values pairs) from a dictionary.
'''

#Q64. What is the use of pop() function?
'''
pop(<key>) is used for deleting the coressponding element from a dicationary
'''

#Q65. What is the use of popitems() function?

'''
popitem() removes the last inserted item from a dicationary.
'''

#Q66. What is the use of keys() function?

'''
keys() returns a list of all the keys present in a dictionary

'''

#Q67. What is the use of values() function?

'''
values() returns a list of all the values present in a dictionary

'''


#Q68. What are loops in Python?

'''
loops are used to do some operations iteratively based on given conditions
''

#Q69. How many type of loop are there in Python?

'''
for loop and while loop
'''

#Q70. What is the difference between for and while loops?

'''
for loop works on known collection
while loop works on some given conditions
'''

#Q71. What is the use of continue statement?

'''
continue statement skips the current iteration and moves to next iteration
'''

#Q72. What is the use of break statement?

'''
break statement breaks out of the current loop and skips all further iterations
'''

#Q73. What is the use of pass statement?

'''
The pass statement is used as a placeholder for future code.
When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.

'''

#Q74. What is the use of range() function?

'''

range() creates a sequence from the start index till end index (end index excluded)
'''

#Q75. How can you loop over a dictionary?

'''
for item in dict_name.items():
'''


### Coding problems
#Q76. Write a Python program to find the factorial of a given number.

num = int(input("Enter the a non negative number:"))
result = 1

while num > 0:
    result = result * num
    num = num - 1
print(result)

#Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100

def getSimpleInterest(p, t, r):
    return (p * r * t)/100
print(getSimpleInterest(100, 5, 10))  # p, t, r can be taken as input


#Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

def getSimpleInterest(p, t, r):
    return p * (1 + r / 100)**t
print(getSimpleInterest(100, 5, 10)) # p, t, r can be taken as input

#Q79. Write a Python program to check if a number is prime or not.

#Q80. Write a Python program to check Armstrong Number.

#Q81. Write a Python program to find the n-th Fibonacci Number.

#Q82. Write a Python program to interchange the first and last element in a list.

#Q83. Write a Python program to swap two elements in a list.

#Q84. Write a Python program to find N largest element from a list.

#Q85. Write a Python program to find cumulative sum of a list.

list1 = [1,2,3,4,5]
result = 0

for num in list1:
    result += num
print(result)

#Q86. Write a Python program to check if a string is palindrome or not.

input_str = input("Enter a string to check pallindrome:") 
if input_str == input_str[-1::-1]:
    print("It is pallindrome")
else:
    print("It is not a pallindrome")


#Q87. Write a Python program to remove i'th element from a string.

#Q88. Write a Python program to check if a substring is present in a given string.

#Q89. Write a Python program to find words which are greater than given length k.

#Q90. Write a Python program to extract unQuire dictionary values.

#Q91. Write a Python program to merge two dictionary.

#Q92. Write a Python program to convert a list of tuples into dictionary.
'''
Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
'''
input = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
output = {}
for pair in input:
    output[pair[0]] = pair[1]
print(output)


#Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
'''
Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
'''
input = [9, 5, 6]
output = []

for num in input:
    output.append((num, num * num * num))
print(output)

#Q94. Write a Python program to get all combinations of 2 tuples.
'''
Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
'''

test_tuple1 = (7, 2) 
test_tuple2 = (7, 8)
output = []

for i in test_tuple1:
    for j in test_tuple2:
        pair_1 = (i,j)
        pair_2 = (j,i)
        output.append(pair_1)
        output.append(pair_2)

print(output)

#Q95. Write a Python program to sort a list of tuples by second item.
'''
Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
'''

#Q96. Write a python program to print below pattern.
'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''
star = "*"
for num in range(1,6):
    i = 1
    while i <= num:
        print(star, end = " ")
        i += 1
    print()

#Q97. Write a python program to print below pattern.
'''
    *
   **
  ***
 ****
*****
'''
star = "*"
space = " "
itr = range(1,6)
for num in itr:
    i = 1
    j = 1
    while len(itr)-num >= i:
        print(space, end = "")
        i += 1
    
    while num >= j:
        print(star, end = "")
        j += 1
    print()

#Q98. Write a python program to print below pattern.
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''

star = "* "
space = " "
itr = range(1,6)
for num in itr:
    i = 1
    j = 1
    while len(itr)-num >= i:
        print(space, end = "")
        i += 1
    
    while num >= j:
        print(star, end = "")
        j += 1
    print()

#Q99. Write a python program to print below pattern.
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
for num in range(1,6):
    i = 1
    while i <= num:
        print(i, end = " ")
        i += 1
    print()
    
#Q100. Write a python program to print below pattern.
'''
A 
B B 
C C C 
D D D D 
E E E E E 
'''
''' 
Approach-1
alphaList = ['A','B','C','D','E']
for num in range(0,5):
    i = 0
    while i <= num:
        print(alphaList[num], end = " ")
        i += 1
    print()
'''
#Approach-2
alpha = 65
for num in range(0,5):
    i = 0
    char = chr(alpha + num)
    while i <= num:
        print(char, end = " ")
        i += 1
    print()
