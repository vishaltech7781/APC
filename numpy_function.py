import numpy as np

arr2 = np.array([[1, 2, 3],
                [ 4, 5, 6]])
arr4 = np.array([[9, 10, 22],
                [ 99, 1,3 ]])

arr3 = np.array([[[1, 2, 3],[ 4, 5, 6]],
                [[7, 8, 9],[10, 11, 12]]])


#max of the array
print("#max of the array")
print(np.amax(arr2))
print(np.amax(arr3))

#min of the array
print("#min of the array")
print(np.amin(arr2))
print(np.amin(arr3))

#index of the max array element
print("index of the max array element")
print(np.argmax(arr2))
print(np.argmax(arr3))

##index of the max array element
print("##index of the max array element")
print(np.argmin(arr2))
print(np.argmin(arr3))

#Computes the cumulative sum of elements in an array along a specified axis.
print("#Computes the cumulative sum of elements in an array along a specified axis.")
print(np.cumsum(arr2))
print(np.cumsum(arr3))

# dot product of the array
print("# dot product of the array")
result1 = np.dot(arr2,arr4.T)
print(result1)

#transpose of the array
print("#transpose of the array 2")
print(arr2.T)
print("#transpose of the array 4")
print(arr4.T)
print("#transpose of the array 3")
print(arr3.T)

#sorting of the array
print("#sorting of the array 4")
print(np.sort(arr4))

print("#addition of the array 2 & 4")
#addition of the array
print(np.add(arr2,arr4))

#substraction of the array
print("#substraction of the array 2 & 4")
print(np.subtract(arr2, arr4))

#multiply of the array
print("#multiply of the array 2 & 4")
print(np.multiply(arr2, arr4))