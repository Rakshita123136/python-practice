#Check an element is in the or not in python example
my_list = ["one","two" , "three" ,"four"]
if"two" in my_list:
    print("'two' is in the list , my_list.");
    print()
    print()
#modified
    my_list = ["one" , "two" ,"three" ,"four"]
    element = input("Enter Element: ")
    if element in my_list:
        print(element, "is in the list , my_list.");
    else:
        print(element, "is not in the list, my_list")
        print()
        print()
