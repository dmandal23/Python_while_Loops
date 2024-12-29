# Counting Positive Number

'''
1. given a list of numbers is

numbers = [1,2,-3,4,5,-6,7,8,-9,10,-11,12,13,-14,15]

2. count all positive number

'''

numbers = [1,2,-3,-4,5,-6,7,8,-9,10,-11,12,13,-14,15]

positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count += 1
print("final count of number is:",positive_number_count)    