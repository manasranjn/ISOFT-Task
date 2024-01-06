set2 = {1,2,3,4,True,False,0}
print(set2)


set1 = set((1,2,3,4))

for x in set1:
    print(x)
    
    
    
set1.add(5)
print(set1)

set1.update(set2)
print(set1)


set2.remove(2)

set2.clear()
del set2

set1 = {"a","b","c"}
set2 = {1,2,3}
set3 =set1.union(set2)