## Assignment Part-1
#Q1. Why do we call Python as a general purpose and high-level programming language?
"""
Python doesn't interact with the machine directly with the machine rather through the interpreter which makes it a HLL. 
Also python is known as a general purpose programming language as it's not for any specific problems but we can use this for
ML, AI, data engineering, software development etc.
"""
#Q2. Why is Python called a dynamically typed language?

""" 
Python is known as dynamically typed language because we don't mention any variable type and the type is determined during runtime.
"""

#Q3. List some pros and cons of Python programming language?

'''
Pros:
    - beginer friendly
    - Extensive libraries
    - Large community
    - Flexible and extensible
    - Easy for AI and ML implementation
    - Highly scalable
    
 Cons:
    - Slower than compiled language
    - Not 100% secure
    - High memory consumption
    - Multithreding
'''

#Q4. In what all domains can we use Python?
'''
- AI
- ML
- web dev
- mobile app dev
- game dev
- data analytics and visualization
- embedded system
'''

#Q5. What are variable and how can we declare them?

'''
Variables are a reference or pointers to an object which stores some values in memory.
<var_name> = <value>
x = 5
y = "hello"
z = int(5)
p = str(1000)
'''

#Q6. How can we take an input from the user in Python?
'''
By using input() we can take inputs in python.

x = input("Enter input:")
'''

#Q7. What is the default datatype of the value that has been taken as an input using input() function?

'''
default datatype of the value that has been taken as an input using input() function is 'string type'
'''

#Q8. What is type casting?

'''
Type casting is to change the type of a variable to another type variable.
'''

#Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

'''
No we can't take multiple inputs with single input() bcoz every input is separated by a new line and in a single line we can take only one input.

But we can achieve this using split() as a hack.
'''

#Q10. What are keywords?
'''
Keywords are the python reserved words used for a special meaning/operation.
'''

#Q11. Can we use keywords as a variable? Support your answer with reason.

'''
No we can't use keywords as a variable as they are meant to do specific operation. So by using that we instruct the interpreter to do a specific operation
and it won't cosider it as a variable.
'''

#Q12. What is indentation? What's the use of indentaion in Python?

'''
Indentation are the white spaces used to indicatcate start of a block of code. As in python we don't use braces to identify block of code, so it uses
indentation to indentify beging and ending of a block of code
'''

#Q13. How can we throw some output in Python?
'''
Using print()
'''

#Q14. What are operators in Python?
'''
Operators are the symbols which is used to do some kind of mathematical/ logical operations
'''

#Q15. What is difference between / and // operators?
'''
'/' is used for division and result a 'float' value
'//' is used for division and result a 'int' value
'''

#Q16. Write a code that gives following as an output.
'''
iNeuroniNeuroniNeuroniNeuron
'''
str = "iNeuron"
print(str*4)

#Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

num = input("Enter the number:")

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

#Q18. What are boolean operator?

'''
and, or, not are the boolean operators
'''

#Q19. What will the output of the following?
'''
1 or 0

0 and 0

True and False and True

1 or 0 or 0
'''

'''
1 or 0 => 1

0 and 0 => 0

True and False and True => False

1 or 0 or 0 => 1
'''


#Q20. What are conditional statements in Python?
'''
if, elif, else are the conditional statements where the corresponding block of code gets executed as per the conditions satisfies.
'''

#Q21. What is use of 'if', 'elif' and 'else' keywords?

'''
if: if the 'if' condition is true then its corresponding block of code will be executed
elif: if the "if" condition fails then elif block condition will be evaluated
else: if all above if or elif conditions fail then atlast else block gets executed
'''

#Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

age = input("Enter the age:")

if age >= 18:
    print("I can vote")
else:
    print("I can't vote")
    
#Q23. Write a code that displays the sum of all the even numbers from the given list.
'''
numbers = [12, 75, 150, 180, 145, 525, 50]
'''

numbers = [12, 75, 150, 180, 145, 525, 50]

def getSum(numbers):
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum +=num
    return sum

print(getSum(numbers))

#Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

num_1 = input("Enter num_1:")
num_2 = input("Enter num_2:")
num_3 = input("Enter num_3:")
greatestNum = num_1

if num_1 >= num_2:
    if num_1 >= num_3:
        greatestNum = num_1
    else:
        greatestNum = num_3
elif num_2 >= num_3:
    greatestNum = num_2
else:
    greatestNum = num_3

print(greatestNum)

#Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
'''
numbers = [12, 75, 150, 180, 145, 525, 50]
'''

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    elif num > 150:
        continue 
    elif  num % 5 == 0:
        print(num)
