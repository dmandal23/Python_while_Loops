# Find Even Numbers
'''
enter a input range
print total even numbers in range

'''

n = int(input("Enter number range:"))

sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += 1

print("sum of even numbers is:",sum_even)        