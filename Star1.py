# First pattern with '@'
for i in range(1, 6):
    for j in range(1, 6):
        if i < 5:
            if j <= i:
                print("@", end=" ")
    print()

# Second pattern with numbers
for i in range(1, 6):
    for j in range(1, 6):
        if i <= 5:
            if j <= i:
                print(i, end=" ")
    print()
