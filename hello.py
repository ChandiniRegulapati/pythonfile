

#Python program to find the factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 0)

                            # Input from the user
    number = int(input("Enter a number: "))

                            # Calculate factorial
    result = factorial(number)

                            # Output the result

    print(f"The factorial of {number} is {result}")



