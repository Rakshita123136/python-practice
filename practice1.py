try:
    t = int(input("Enter the number of test cases: "))
    while t != 0:
        n = int(input("Enter the size of the array: "))  # Example: 4
        arr = []
        for i in range(n):
            arr.append(list(map(int, input("Enter row {} of the array: ".format(i+1)).split())))
        
        count = 0
        for i in range(n):
            for j in range(n):
                for p in range(i, n):
                    for q in range(j, n):
                        if arr[i][j] > arr[p][q]:
                            count += 1
        print("Number of inversions:", count)
        t -= 1
except ValueError as e:
    print("Invalid input! Please enter valid integers.")
#output
#Enter the number of test cases: 1
#Enter the size of the array: 4
#Enter row 1 of the array: 1 2 3 4
#Enter row 2 of the array: 1 3 4 5
#Enter row 3 of the array: 2  4 5 6
#Enter row 4 of the array: 1  3 4  5
#Number of inversions: 4
