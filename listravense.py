squares = []
for i in range(12):
    squares.append(i*2)
    print(squares)
    print()
    
my_list = []
for x in [8,4,5]:
    for y in [3,5,2]:
        if x != y:
            my_list.append((x,y))
            print(my_list)
            print()
            
a = [-2,-4,2,3,0]
print([m*2 for m in a])
print([abs(m) for m in a])
print()
print()
list=['red','green','blue','yellow','white']
print([x.strip() for x in list])
