#deleting elements from list in python example
my_list = ["zero" , "one", "two" , "three" ,"four"]
print("Elements of the list, my_list are:")
for ml in my_list:
    print(ml)
index = input("Enter index no:")
index = int(index)
print("Deleting the element present at index number " ,index)
del my_list[index]
print("Now elements of the list , my_list are:")
for ml in my_list:
    print(ml)
    print()
      
