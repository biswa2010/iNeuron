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

#Q33. How can you print the below string?
'''
'iNeuron's Big Data Course'
'''
string = "'iNeuron\'s Big Data Course'"
print(string)

#Q34. What is a list in Python?

#Q35. How can you create a list in Python?

#Q36. How can we access the elements in a list?

#Q37. Write a code to access the word "iNeuron" from the given list.
'''
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
''' 

#Q38. Take a list as an input from the user and find the length of the list.

#Q39. Add the word "Big" in the 3rd index of the given list.
'''
lst = ["Welcome", "to", "Data", "course"]
'''

#Q40. What is a tuple? How is it different from list?

#Q41. How can you create a tuple in Python?

#Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.

#Q43. Can two tuple be appended. If yes, write a code for it. If not, why?

#Q44. Take a tuple as an input and print the count of elements in it.

#Q45. What are sets in Python?

#Q46. How can you create a set?

#Q47. Create a set and add "iNeuron" in your set.

#Q48. Try to add multiple values using add() function.

#Q49. How is update() different from add()?

#Q50. What is clear() in sets?

#Q51. What is frozen set?

#Q52. How is frozen set different from set?

#Q53. What is union() in sets? Explain via code.

#Q54. What is intersection() in sets? Explain via code.

#Q55. What is dictionary ibn Python?

#Q56. How is dictionary different from all other data structures.

#Q57. How can we delare a dictionary in Python?

#Q58. What will the output of the following?
'''
var = {}
print(type(var))
'''

#Q59. How can we add an element in a dictionary?

#Q60. Create a dictionary and access all the values in that dictionary.

#Q61. Create a nested dictionary and access all the element in the inner dictionary.

#Q62. What is the use of get() function?

#Q63. What is the use of items() function?

#Q64. What is the use of pop() function?

#Q65. What is the use of popitems() function?

#Q66. What is the use of keys() function?

#Q67. What is the use of values() function?

#Q68. What are loops in Python?

#Q69. How many type of loop are there in Python?

#Q70. What is the difference between for and while loops?

#Q71. What is the use of continue statement?

#Q72. What is the use of break statement?

#Q73. What is the use of pass statement?

#Q74. What is the use of range() function?

#Q75. How can you loop over a dictionary?


### Coding problems
#Q76. Write a Python program to find the factorial of a given number.

#Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100

#Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

#Q79. Write a Python program to check if a number is prime or not.

#Q80. Write a Python program to check Armstrong Number.

#Q81. Write a Python program to find the n-th Fibonacci Number.

#Q82. Write a Python program to interchange the first and last element in a list.

#Q83. Write a Python program to swap two elements in a list.

#Q84. Write a Python program to find N largest element from a list.

#Q85. Write a Python program to find cumulative sum of a list.

#Q86. Write a Python program to check if a string is palindrome or not.

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

#Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
'''
Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
'''

#Q94. Write a Python program to get all combinations of 2 tuples.
'''
Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
'''

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

#Q99. Write a python program to print below pattern.
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''

#Q100. Write a python program to print below pattern.
'''
A 
B B 
C C C 
D D D D 
E E E E E 
'''
