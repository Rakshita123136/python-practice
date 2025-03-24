a = -30
b = 30

print("1" , "a =" , a, ":" , id(a), "b=" ,b,":" , id(b))
if (a is b):
    print("a and b have same identity")
else :
    print("a and b do not have same identity")
if(id(a) == id(b)) :
    print("a  and b do not have same identity")
else :
    print("a  and b do not have same identity")

b = 40
print("a =" ,a, ":",id(a), "b=",b, ":", id(b))
if(a is not b):
    print("a=" ,a, ":" ,id(a) , "b=" ,b, ":" , id(b))
else :
    print("a and b have same identity") 
