Python OOP Assignment
Q1. What is the purpose of Python's OOP?

'''
The purpose of python's oops concept is to implement the real life entities like inheritance, polymorphism, encaptulation etc. using programatically
'''

Q2. Where does an inheritance search look for an attribute?

'''
- First searches in the instance object
- Then in the class from where instance created
- Then searches in its parent classes until it finds the attribute for the first time.
'''

Q3. How do you distinguish between a class object and an instance object?

'''
Class is like a blue print and object is the instance of a class
'''

Q4. What makes the first argument in a class’s method function special?

'''
The first argument of a class method is the reference to the same object by which the method is called.
'''

Q5. What is the purpose of the init method?

'''
init method is used to initialize the object attributes

'''

Q6. What is the process for creating a class instance?

'''
ref = ClassName(<arguments >)
'''

Q7. What is the process for creating a class?

'''
class ClassName:
    attributes
    init method
    other methods
'''


Q8. How would you define the superclasses of a class?

'''

class className(SuperclassName):
    attributes
    methods
'''

Q9. What is the relationship between classes and modules?

'''

Modules are collections of methods and constants. They cannot generate instances. 
Classes may generate instances , and instance variables

'''

Q10. How do you make instances and classes?

'''

class ClassName:
    def __init__(self, name):
        self.name = name

obj = ClassName("Hello")


'''


Q11. Where and how should be class attributes created?

'''
Class attributes should be created inside a class but not defined inside __init_()

class Hello:
    class_attribute=5

'''


Q12. Where and how are instance attributes created?

'''
Instance attributes should be created inside __init__ method

class ClassName:
    def __init__(self, name):
        self.name = name

'''

Q13. What does the term "self" in a Python class mean?

'''
self represents the instance of the class while calling any methods or while creating an object.
'''

Q14. How does a Python class handle operator overloading?

'''
In python we don't have over loading. So it uses conditions in side a method to perform differently
'''

Q15. When do you consider allowing operator overloading of your classes?

''' 
Whenever any same operator being used for 2 or more ways then we can consider
'''

Q16. What is the most popular form of operator overloading?

''' 
+ operator is a most popular operator overloading
'''

Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?

'''
Inheritance
Pollymorphisim

'''

Q18. Describe three applications for exception processing.

'''
Creating/closing a DB connection
Accessing files
Handling date processings
while accessing empty collections

'''

Q19. What happens if you don't do something extra to treat an exception?

''' 
Then it terminates as and when any exception happens
'''

Q20. What are your options for recovering from an exception in your script?

'''
- catch the exception and ignore/ or do nothing
- Catch the exception and do some other logic
- Do something in the finally block for all the exception occured

'''

Q21. Describe two methods for triggering exceptions in your script.

''' 
try and raise
'''

Q22. Identify two methods for specifying actions to be executed at termination time, regardless of whether or not an exception exists.

''' 
- finally
- else
'''

Q23. What is the purpose of the try statement?

'''
try statement is used to enclose the ecception occuring codes.
'''

Q24. What are the two most popular try statement variations?

'''
- try with except
- try with except  and finally
'''

Q25. What is the purpose of the raise statement?

''' 
To raise and exception intentionally we use raise statement.
'''



Q26. What does the assert statement do, and what other statement is it like?

''' 
assert keyword used to check some condition. If the condition returns false then it gives error or it prints a message
it hass various methods too to do assertion for
'''

Q27. What is the purpose of the with/as argument, and what other statement is it like?

''' 
with - to simplyfy exception code
as - used as alias
'''

Q28. What are *args, **kwargs?

''' 
*args (to accept Non-Keyword Arguments in a method)
**kwargs (to accept Keyword Arguments in a method)

'''

Q29. How can I pass optional or keyword parameters from one function to another?

''' 
using *args and **kwargs
'''

Q30. What are Lambda Functions?

''' 
It's an annonymous function which accepts arguments and then evaluates defined expression
'''

Q31. Explain Inheritance in Python with an example?

''' 
Inheritance is aquiring/reusing some properties from a parent class to base class

class A:
    #define init()
    def hello(self):
class B(A):


Here hello method will be available in class B as well
'''

Q32. Suppose class C inherits from classes A and B as class C(A,B).Classes A and B both have their own versions of method func(). If we call func() from an object of class C, which version gets invoked?

''' 
Class A version will be used
'''

Q33. Which methods/functions do we use to determine the type of instance and inheritance?

''' 
isinstance()
issubclass()
'''

Q34.Explain the use of the 'nonlocal' keyword in Python.

''' 

The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.

'''


Q35. What is the global keyword?

''' 
global keyword is being used  in a local method to access the global variable

'''
