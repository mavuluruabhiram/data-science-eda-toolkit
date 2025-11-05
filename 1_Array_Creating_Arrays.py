#Importing
import numpy as np

#creating array

arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3],
                 [3, 4, 5.6]])

arr3 = np.array((1, 2, 3,6,7,8,))   # [ ---- ] 

print('arr1 : ' , arr1)
print('arr2 : ' , arr2)
print('arr3 : ' , arr3)

#ASARRAY METHOD

print('\ncreating array using Asarray method\n')

a = [10,20,30,40]
f = np.asarray(a,dtype=float)
i = np.asarray(a,dtype=int)
print('float : ' , f)
print('Int : ' , i)

# FROM BUFFER METHOD 

print('\nFROM BUFFER METHOD\n')

p = b'welcome abhiram reddy'
k=np.frombuffer(p,dtype='S1')
print('from buffer :' , k)

p = b'welcome abhiram reddy'
l=np.frombuffer(p,dtype='S1' , count=10)  #upto 10 values
print('from buffer :' , l)

p = b'welcome abhiram reddy'
m=np.frombuffer(p,dtype='S1' , count=10 , offset=10)     #upto 10 values starts from 11th
print('from buffer :' , m)

print('\n---=-- INITIALIZING OF ARRAYS ------\n')

# Zero Array
arr5 = np.zeros((3,4))   # Default Float
arr4 = np.zeros((3,3) , dtype=int)

# Ones Array
arr6 = np.ones((3,4))   # Default Float
arr7 = np.ones((3,3) , dtype=int)

# Full Funtion

arr8 = np.full((2,5),7)   # 2 by 3 matrix with 7

# Eye Function - Identity Matrix

arr9 = np.eye(3)  # order 3 Identity matrix



# Arange Funtion

seq1 = np.arange(5)
seq2 = np.arange(1,10,2)       # print 1 to 10 by 2 space

#Lin Space Funtion - linearly space values - used to generate Num between 2 num which are equaly spaced

# ( start , end ,  no.of parts )

lin1 = np.linspace(0, 1, 5 , retstep=True)   # retstep tells by what nm is divided 
lin2 = np.linspace(1, 20, 33)

#Random Funtion - gives random values       1 random.rand   2. random.randint

rand1 = np.random.rand(2,3)

rand2 = np.random.randint(1,10 ,(4,3))

#astype function 

ass = np.array([1.0 , 2.0 , 3.0])
ass = ass.astype(int)


print("\n----------\n")
print(type(arr1))  # <class 'numpy.ndarray'>
print('arr4 : ' , arr4) 
print('arr5 : ' , arr5)
print('arr6 : ' , arr6)
print('arr7 : ' , arr7)
print('arr8 : ' , arr8)
print('arr9 : ' , arr9)
print("\n-----RANGE FUNCTION-----\n")
print('seq1 :' , seq1)
print('seq2 :' , seq2)

print("\n-----LIN SPACE FUNTION-----\n")
print('lin1: ' , lin1)
print('lin2: ' , lin2)

print("\n-----RANDOM FUNCTION-----\n")
print('rand1 : ' , rand1)
print('rand2 : ' , rand2)

print("\n-----ASTYPE FUNCTION-----\n")
print('astype : ' ,ass)





print(' \n------- ARRAY OPERATIONS -------\n ')

# INDEXING  

print("\n-----SLICING & INDEXING -----\n")

arr = np.arange(1,21).reshape(4,5) 
print(arr)
print(arr[0])  # Prints 1st Row
print(arr[1])  # Prints 2nd Row
print(arr[0,])  # Prints 1st Row
print(arr[1,2])  # Prints 2nd Row 3rd element

# SLICING 
print(arr[1 , 2 : 4])  # Starts from 2nd row 3rd element  to 5th element ( 5th not included )

# RESHAPE METHOD

print("\n-----RESHAPE METHOD -----\n")

res = np.arange(12)             #  only we can reshape with multiples of 12
print('reshape : ',res)

res1 = res.reshape(2,6)
print('reshape1 : ',res1)

res2 = res.reshape(3,4)
print('reshape2 : ',res2)


#Shape
print(arr1.shape)   # 3 columns
print(arr2.shape)   # 2 rows & 3 columns
print(arr3.shape)

#No.Of Attributes
print(arr1.size)   
print(arr2.size) 
print(arr3.size) 

#DataTypes
print(arr1.dtype)   
print(arr2.dtype) 
print(arr3.dtype) 

f2 = np.array([[1,2,3] , [4,5,6] , [7,8,9]])

print('\n' , f2)

print( f2 [ [0,2] , [1,2] ] )