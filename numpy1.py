#ndarray - array object
import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)


arr1 = np.array(43)

arr2 =  np.array([[1, 2, 3], [4, 5, 6]])

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])


print(arr2[1,1])
print(arr2[1,-1])
print(arr2.ndim)


#numpy array slicing

# [start:end]
# [start:end:step]


arr = np.array([1,2,3,4,5,6,7,8])
print(arr[1:5])
print(arr[-3:-1:2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1,1:4])
print("shape of array ",arr.shape)

arr1 = np.array([1,2,3,4],dtype="S")
print(arr1.dtype)


# arr1 = np.array(['a','b','c'],dtype="i")


#copying an array


arr2= np.array([1,2,3,4])
x = arr2.copy()
y=arr2.view()
arr2[1]=45
y[2]=34
x[2]=55

print(x)
print(y)
print(arr2)

#array view


#array shape / reshape
#The shape of an array is the number of 
# elements in each dimension.




array1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
array2 = array1.reshape(4,3)
print(array2)

#flatten array

arr1 = np.array([[1,2,3,4],[2,3,4,5]])
n1 = arr1.reshape(-1)
print(n1)



for i in arr1:
    for j in i:
        print(j)
        
        
#nditer()


arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("printing 3d array")
for i in np.nditer(arr):
    print(i)
    
    
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr =  np.concatenate((arr1,arr2))
print(arr)


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])


arr = np.concatenate((arr1,arr2),axis=1)
print(arr)


arr = np.concatenate((arr1,arr2),axis=0)
print(arr)


arr = np.hstack((arr1,arr2))
print(arr)
arr = np.vstack((arr1,arr2))
print(arr)


#splitting of an array
