no = int(input("Enter the number: "))
numbers = [23, 33, 45, 65, 22, 88, 44, 67, 70]
found = False

for i in numbers:
    if i == no:
        print("Number Found in the List")
        found = True
        break

if not found:
    print("Number not found in the list")
