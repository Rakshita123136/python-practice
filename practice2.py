# Cyclic Shift
# A large binary number is represented by a string 's' of size 'n' and comprises of 0s and 1s.
# You must perform a cyclic shift on this string. The cyclic shift operation is defined as follows:
# If the string 's' is 'abcdef', then after performing one cyclic shift, the string becomes 'bcdefa'.
# You performed the shift an infinite number of times and each time you recorded the value of the binary number represented by the string.
# The maximum binary number formed after performing (possibly 0) the operation is 'max_s'.
# Your task is to determine the number of cyclic shifts that can be performed such that the value represented by the string 's' will be equal to 'max_s' for the 'k-th' time.

# Read the number of test cases
t = int(input())

# Process each test case
while t != 0:
    # Read the values of n and k
    n, k = map(int, input().split())
    # Read the string s
    s = input()
    
    max_str = ""  # Initialize max_str as an empty string
    p = -1  # Initialize p as -1
    
    for i in range(n):
        # If max_str is less than the current string s
        if max_str < s:
            max_str = s  # Update max_str with s
            d = i  # Update d with the current index
        elif max_str == s:
            # If max_str is equal to the current string s
            p = i - d  # Update p with the difference between current index and d
            break  # Exit the loop
        
        # Rotate the string s by moving the first character to the end
        s = s[1:] + s[0]

    # If p is still -1, it means no second occurrence was found
    if p == -1:
        print(d + (k - 1) * n)  # Output the position
    else:
        print(d + (k - 1) * p)  # Output the position

    # Print a blank line
    print(" ")
    
    # Decrement the test case counter
    t -= 1

