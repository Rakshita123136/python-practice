# Minimum AND xor OR
# Given an array 
#  A of N integers. Find out the minimum value of the following expression for all valid i,j


t = int(input())
while t != 0:
    n = int(input())
    arr = list(map(int, input().split()))  # Fixed the split() method call
    arr.sort()
    min_xor = arr[0] ^ arr[1]
    for i in range(1, n - 1):
        temp = arr[i] ^ arr[i + 1]
        if temp < min_xor:
            min_xor = temp
    print(min_xor)  # Moved print statement outside the loop
    t -= 1  # Corrected decrement of t
