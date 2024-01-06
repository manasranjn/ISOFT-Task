myList = ["a","b","c","d","a"]
print(myList)


#List items are ordered, 
# changeable, and allow duplicate values.

print(len(myList))

mylist1=[1,2,3,"a",False,"b","e","f",5,6,7,8,9]

thislist = list(("a","b","c"))
print(thislist)

print(thislist[-1])

print(mylist1[2:5])  #end not included

print(mylist1[:5])

print(mylist1[2:])


print(mylist1[-6:-1])

if "a" in mylist1:
    print("yes")
else:
    print("not")
    
# mylist1=[1,2,3,"a",False,"b","e","f",5,6,7,8,9]

mylist1[4] = True
print(mylist1)

mylist1[8:11] = [11,12,13]

print(mylist1)

mylist1.insert(2,22)
print(mylist1)
mylist1.append("yellow")
print(mylist1)

list1=[1,2,3,4]
list2=[5,6,7,8]
list1.extend(list2)
print(list1)

mylist1.remove(22)
print(mylist1)

mylist1.pop(4)
print(mylist1)

del mylist1[0]
print(mylist1)


# mylist1.clear()

# for i in range(len(mylist1)):
#     print(mylist1[i])
    
i=0  
while i<len(mylist1):
    print(mylist1[i])
    i=i+1
    
#list comprehension
vegetables = ["tomatoes","potatoes","onion","okra","brocolli","eggplany"]
newList =[]

for i in vegetables:
    if "b" in i:
        newList.append(i)
print(newList)

newList1 = [x for x in vegetables if "b" in x]
print(newList1)


#newlist = [expression for item in iterable if condition == True]

vegetables.sort(reverse=True)
print(vegetables)

vegetables.reverse()
print(vegetables)


str = "swati"
del str
print(str)