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
