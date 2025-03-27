# Question:
# Given a number n, for each integer i in the range from 1 to n (inclusive), print one value per line as follows:

# If i is a multiple of both 3 and 5, print FizzBuzz.

# If i is a multiple of 3 (but not 5), print Fizz.

# If i is a multiple of 5 (but not 3), print Buzz.

# If i is not a multiple of 3 or 5, print the value of i.

# Import sys to read input from stdin, useful for competitive programming platforms like HackerRank
import sys

# Read the input value as an integer
n = int(sys.stdin.readline().strip())

# Define the fizzBuzz function
def fizzBuzz(n):
    # Loop through numbers from 1 to n
    for i in range(1, n + 1):
        # Check if the number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")  # Print "FizzBuzz" for multiples of both 3 and 5
        # Check if the number is divisible by only 3
        elif i % 3 == 0:
            print("Fizz")  # Print "Fizz" for multiples of 3
        # Check if the number is divisible by only 5
        elif i % 5 == 0:
            print("Buzz")  # Print "Buzz" for multiples of 5
        else:
            print(i)  # Print the number itself if none of the conditions match

# Call the fizzBuzz function with the input value
fizzBuzz(n)
