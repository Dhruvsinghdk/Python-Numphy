import numpy as np

# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]

# n1 = np.array([[10,20,30,40,50],[60,70,80,90,100]])
# n2 = np.array([[l1],[l2]])
# print(n2)

# initializing arr zeros
# n1 = np.zeros((5,5))

# print(n1)

# initializing full array

# n3 = np.full((3,2),22)
# print(n3)

# initializing array  within range
# n4 = np.arange(10,20)
# print(n4)
# print()
# n1 = np.arange(10,30,3)
# print(n1)

# random value

# n1 = np.random.randint(1,10,10)
# print(n1)

# checking shape of array
# n = np.array([[10,20,30],[40,50,60]])

# print(n.shape)

# n.shape = (3,2)
# print(n.shape)
# print(n)


# joining numpy array
# n1 = np.array([10,20,30,40])
# n2 = np.array([50,60,70,80])

# n = np.vstack((n1,n2))
# print(n)

# Numpy intersection
# n1 = np.array([10,20,30,40])
# n2 = np.array([40,50,60,70])
# n = np.intersect1d(n1,n2)
# print(n)


# n1 = np.array([10,20,30,40])
# n2 = np.array([40,50,60,70])
# n = np.setdiff1d(n1,n2)
# print(n)

# n1 = np.array([10,20,30,40])
# n2 = np.array([40,50,60,70,80])
# n = np.setdiff1d(n2,n1)
# print(n)

# Addition of array

# n1 = np.array([10,20])
# n2 = np.array([30,40])
 
# n = np.sum([n2])
# n2 = np.sum([n1,n2])
# print(n2)

# n1 = np.array([10,20,30,40])
# n2 = np.array([40,50,60,70])
# n = np.sum([n1,n2],axis=1)
# print(n)

# basic maths
# n1 = np.array([10,20,30])
# n1 = n1*2 
# print(n1)


# basic maths function
# n1 = np.array([10,20,30,40,22,45])
# n2 = np.mean(n1)
# print(n2)

# median
# n1 = np.array([10,20,30,40,22,45,11,22])
# n2 = np.median(n1)
# print(n2)

# standard deviation
# n1 = np.array([10,20,30,40,22,45,11,22])
# n2 = np.std(n1)
# print(n2)


# Numphy save and load
n1 = np.array([10,20,30,40,50])
n1 = np.save('myarray',n1)


n2 = np.load('myarray.npy')
print(n2)
