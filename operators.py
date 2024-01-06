#operators are constructs which manipulates the value of an operanad


# expression 3+7 = 10 
#3,7 opearnds
# + is an operator
#10 result 


# Arithmetic Operators
# mathematical operations

# +.-,*,/,%,**,//

a=21
b=10

#add
print("a+b :",a+b)

#minus
print("a-b : ",a-b)

#multiply
print("a*b : ",a*b)

# Division
print ("a / b : ", a / b)

# Modulus
print ("a % b : ", a % b)

# Exponent
print ("a ** b : ", a ** b)

# Floor Division
print ("a // b : ", a // b)


# Comparison (Relational) Operators
# ==	Equal	                    4 == 5         is not true.
# !=	Not Equal	                4 != 5         is true.
# >	Greater Than	            4 > 5          is not true.
# <	Less Than	                4 < 5          is true.
# >=	Greater than or Equal to	4 >= 5         is not true.
# <=	Less than or Equal to	    4 <= 5         is true.


a=4
b=5

#Equal
print("a == b :",a == b)

#Not Equal
print("a != b :",a != b)

#greater than
print("a > b :",a > b)

#less than
print("a < b :",a < b)

#greater tahn equalto
print("a >= b :",a >= b)

#less than equal to
print("a <= b :",a <= b)


# Assignment Operators
t = 20

t += 5
print("t += 5",t)

t -= 5
print("t -= 5",t)

t *= 5
print("t *= 5",t)

t /= 5
print("t /= 5 ",t)

t %= 3
print("t %= 3",t)

t **= 2
print("t **= 2",t)

t //= 3
print("t //= 3", t)


# Logical Operators
# x=6
# y=9

# and    x>5 and y>10  true
# or     x>5 or y>10 true
# not   not ( x>5 and y>8)  - false

x = 5

print(x > 3 and x < 10)

print(x > 3 or x < 4)

print(not(x > 3 or x < 4))

# Bitwise Operators
# Membership Operators
j = ["a","b","c","d"]

print("c in j","c"in j)
print("a not in j","a" not in j)


# Identity Operators
#compare the objects
# is true/false x is y
# is not   x is not y

x = ["a","b"]
y = ["a","b"]
z=x

print("x is y",x is y)
print("x is z",x is z)

print("x is not z",x is not z)
print("x is not y",x is not y)

print("x == y",x == y)


a =10
b=4

print("a & b : ",a&b)

print("a | b : ",a|b)

print("~a : ",~a)

print("a ^ b : ",a^b)