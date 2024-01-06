mytuple = ("a","b","c","a")
print(mytuple)
print(len(mytuple))

mytup1= (1,"a")
print(type(mytup1))

tup1 = tuple((1,2,3,4))

print(tup1[2])


# creqte a simple tuple with 10 items in it
# access the 6th item from it
# then with the help of negative indexing
# access the 3rd,5th, 8th item 
# then use range of indexes to return the 3rd, 4th and 5th item
# use -ve indexing to retun items from the 2nd posiiton till last - 1


tup1 = (1,2,3,4,5)
if 6 in tup1:
    print("yes")
else:
    print("NO")
    
    
tup2 = (1,2,3,4,5)
list1 = list(tup2)

list1[2]=7

tup2=tuple(list1)

print(tup2)

letters =("A","B","C","D")
numbers=(1,2,3,4)
(a,b,*c)=letters  #unpacking
print(a)
print(c)

for x in letters:
    print(x)
    
print(letters+numbers)
print(letters*2)