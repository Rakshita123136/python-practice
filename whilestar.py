i = 0
while i < 5:
    j = i + 1
    while j > 0:
        print("$", end="")
        j = j - 1
    i = i + 1  # This should be i = i + 1
    print()

print()

i = 1
while i < 6:
    j = 1
    while j <= i:
        print(i, end="")
        j = j + 1
    i = i + 1
    print()
    
