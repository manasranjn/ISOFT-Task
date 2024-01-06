dict1={
    "fname":"Swati",
    "lname":"yadav"
}

dict1["fname"] = "Arya"
print(dict1)
print(len(dict1))
print(dict1.get("lname"))
print(dict1["fname"])
print(dict1.keys())
print(dict1.values())
print(dict1.items())

thisdict = dict(name="swati",age=30)
print(thisdict)


if "lname" in dict1:
    print("yes")
    
    
dict1.update({"age":30})
print(dict1)


dict1["address"]="lucknow"
print(dict1)

# dict1.pop("lname")
# dict1.popitem()
# del dict1["lname"]
# dict1.clear()


for i in dict1:
    print(i)
    print(dict1[i])
    
    
for i in dict1.values():
    print(i)

for i in dict1.keys():
    print(i)
    
for i in dict1.items():
    print(i)
  
  
# i=0  
# while i<len(dict1):
    
#     print(dict1[i])
#     i+=1
    
    
dict2 = dict1.copy()
    
dict3 = dict(dict1)