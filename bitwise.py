a = 63
b = 13
print("a=" ,a, ':' , bin(a) , "b =" ,b, ":" , bin(b))
c = a & b
print("Result of bitwise AND is " , c , ':' ,bin(c))
c = a | b
print("Result of bitwise OR is " , c, ':' ,bin(c))
c = a ^ b
print("Result of bitwise XOR is " , c, ':' ,bin(c))
c =~ a
print("Result of complete is " ,c, ':' ,bin(c))
c = a << 2
print("Result of left shift is" , c, ':' ,bin(c))
c = a >> 2
print("Result of Right shift is " ,c, ':' ,bin(c))
