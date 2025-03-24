money = int(input("Enter the Amount: "))
if(money < 1000):
    discount = money*0.10
    print("Discount for amount <1000 is",discount)
elif(money<5000):
    discount = money*0.20
    print("Discount for amount < 5000 is",discount)
elif(money<10000):
    discount = money*0.30
    print("Discount for amount < 1000 is",discount)
else:
    discount = money*0.05
    print("Net payable amount is" , dicount)
