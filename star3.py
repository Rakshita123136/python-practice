for i in range(1, 6):
    for j in range(1, 6):
        if i < 5:
            if j <= i:
                print(j, end="")
    print()
for i in range(1, 6):
    for j in range(1, 6):
        if i <= 5:
            if j <= i:
                print("*", end="")
    print()
i = 5
while i >= 1:
    j = 1
    while j <= i:
        print(i, end="")
        j += 1
    print()
    i -= 1
