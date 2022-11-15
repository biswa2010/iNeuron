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
