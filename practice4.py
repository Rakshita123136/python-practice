# Monk and Rotation
# This program rotates an array to the right by K steps.
# Given an integer array A of size N and an integer K, we need to shift all elements K times to the right.
# The challenge is to do this efficiently without using extra space for a new array.

t = int(input())  # Number of test cases

while t != 0:
    # Read the values of N (size of array) and K (rotation count)
    n, k = map(int, input().split())
    
    # Read the array elements
    arr = list(map(int, input().split()))  

    # Calculate the starting index after rotation
    # Since rotating by N times brings the array back to its original form, we use (K % N)
    index = n - (k % n)  

    # Print the rotated array by first printing the last (K % N) elements
    for i in range(index, n):
        print(arr[i], end=" ")  
    
    # Print the remaining elements from the beginning
    for i in range(index):
        print(arr[i], end=" ")  

    print()  # Print a newline for better readability
    
    t -= 1  # Reduce test case count
