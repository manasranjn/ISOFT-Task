txt = "hello, and welcome to my world."
print(txt.capitalize())

print(txt.count("e"))

print(txt.startswith("h",5,11))


print(txt.find("swati"))


print(txt.index("my"))

txt1 = "hello"
x=txt1.center(30,"@")
print(x)



# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string



# A string is considered a valid identifier if it only 
# contains alphanumeric letters (a-z) and (0-9), or underscores (_).
# A valid identifier cannot start with a number, or contain any spaces.



a = "myFolder"
b="123thf"
c="@hhjs"
d="my name"
e="_vsdf"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
print(e.isidentifier())


txt3="Hello\rhow are you?"

print(txt3.isprintable())
print(txt3)


print('pyhton is fun to leran\r12344567')



a="HELLO MY NME IS"
b="Hello World"
c="Hello"
d="12 years"
e="this is @@@"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())
print(e.istitle())



myTuple = ("A","B","C")
print("@".join(myTuple))


txt = "apple"
x=txt.ljust(20,"-")
y=txt.rjust(20,"-")
print(x,"is my fav fruit")
print(len(x))

txt="              abc                "
x=txt.lstrip()
y=txt.rstrip()
print("ABC",x,"der")
print("ABC",y,"der")