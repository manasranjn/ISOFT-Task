str = '''String'''
# print(type(str))
print(str[3])
# print(str[8])



# HELLO
# 01234

# length - 5

# str[:] = HELLO
# str[0:] = HELLO
# str[:5] = HELLO
# str[2:5] = LLO

# str[-4:] = ELLO
# str[:-1]= HELL
# str[::-1] = OLLEH
# str[-5:-3] = HE

# H  E L L O
# -5-4-3-2-1

for i in str:
    print(i)
    
print(len(str))

#in
text = "my name is swati yadav"
print("name" not in text)

a = "swati"
y = "yadav"
c=a+" "+y
print(c)

print(a.upper())

b="    SWATI      "
print(b.lower())
print(len(b))

t=b.strip()
print(len(t))
print(b.strip())

print(b.replace("S","W"))

str1 = "Hello, World"
print(str1.split(","))

# String formatting

# abc = "swati"
# x=67
# txt=abc+x
# print(txt)

#format()
#

number = 20
n1=30
txt1 = "i scored {0} out of {1} in my \"test\" today"
print(txt1.format(number,n1))
