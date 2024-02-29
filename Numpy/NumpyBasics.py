#importing
import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # 1x5 vector

print(array.shape)

a = array.reshape(3,5) # 3x5 matrix

print("Shape:",a.shape)
print("Dimension:",a.ndim)

print("Data type:",a.dtype.name)
print("Size:",a.size)

print("type:",type(a))

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])

print(array1)
print(array1.shape)

zeros = np.zeros((3,4))
zeros[1,2] = 6

print(zeros)

one = np.ones((3,3))
print(one)

empty = np.empty((3,4))
print(empty)

v = np.arange(10,50,5)
print(a)

x = np.linspace(10,50,20)
print(x)

# Basic Operations
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)
print(np.sin(a))
print(a<2)

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])
print(a*b)

print(a.dot(b.T))

print(np.exp(a))

a = np.random.random((4,4))
print(a)

print(a.sum())
print(a.max())
print(a.min())

print(a.sum(axis=0))
print(a.sum(axis=1))

print(np.sqrt(a))
print(np.square(a))

print(np.add(a,a))

#indexing and slicing
array = np.array([1,2,3,4,5,6,7]) # vector dimension = 1

print(array[0:4])

reverse_array = array[::-1]
print(reverse_array)

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array1[1,2])
print(array1[:1])
print(array1[1,1:4])

print(array1[-1,:])
print(array1[:,-1])

#shake manipilation
array = np.array([[1,2,3],[4,5,6],[7,8,9]])

#flatten
a = array.ravel()
print(array)
print(a)

array2 = a.reshape(3,3)
print(array2)

arrayT =array2.T
print(arrayT)
print(arrayT.shape)

array5 = np.array([[1,2],[3,4],[5,6]])
print(array5.reshape(2,3))
print(array5)

#stacking arrays

array1 = np.array([[1,2],[3,4]])

array2 = np.array([[-1,-2],[-3,-4]])

print(array1,array2)


array3 = np.vstack((array1,array2))

print(array3)

array3 = np.hstack((array1,array2))

print(array3)

#convert and copy

liste = [1,2,3,4] #list

array = np.array(liste) #np.array

print(array)

liste2 = list(array)
print(liste2)


a = np.array([1,2,3])
b = a
c = a
print(a,b,c)

b[0] = 5
print(a,b,c)

d = np.array([1,2,3])
e = d.copy()
f = d.copy()

print(d,e,f)
f[0] = 5

print(d,e,f)