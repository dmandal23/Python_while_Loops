# Factorial Calculator using while loop 

number = int(input("Enter number"))
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1


print("factorial is:", factorial)

