import sys
import numpy as np
a=np.array([1,2,3,4])
b=np.array([0,.5,1,1.5,2])
print(a[0],a[1])
print(a[0:])
print(a[1:3])
print(a[1:-1])
print(a[::2])
print(b[0],b[2],b[-1])
print(b[[0,2,-1]])
print(a.dtype)
print(b.dtype)
print(np.array([1,2,3,4],dtype=np.float32))
print(np.array([1,2,3,4],dtype=np.int8))
c=np.array(['a','b','c'])
print(c.dtype)
d=np.array([{'a':1},sys])
print(d.dtype)
print("---------dimension and shape-----------")
A=np.array([[1,2,3],[4,5,6]])
print(A.shape)
print(A.ndim)
print(A.size)
print("---------array B----------")
B=np.array([
    [[12,11,10],[9,8,7]],
    [[6,5,4],[3,2,1]]
])
print(B.shape)
print(B.ndim)
print(B.size)


print("------Indexing and Slicing Matrices-------")
A=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
            ])
print(A[1])
print(A[1][0])
print(A[1,0])
print(A[0:2])
print(A[:,:2])
print(A[:2,:2])
print(A[:2,2:])
A[1]=np.array([10,10,10])
print(A)
A[2]=99
print(A)
print("-------Summary Statistics---------")
a=np.array([1,2,3,4])
print(a.sum())
print(a.mean())
print(a.std())
print(a.var())
A=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(A.sum())
print(A.mean())
print(A.std())
print(A.sum(axis=0))
print(A.sum(axis=1))
print(A.mean(axis=0))
print(A.mean(axis=1))
print(A.std(axis=0))
print(A.std(axis=1))

print("------broadcating and vectorized operation-------")

a=np.arange(4)
print(a)
print(a+10)
print(a*10)
print(a)
a=a+100
print(a)

b=np.array([10,10,10,10])
print(b)
print(a+b)
print(a*b)

print("---------Boolean arrays---------")
a=np.arange(4)
print(a)
print(a[[0,-1]])
print(a[0],a[-1])
print(a[[True,False,False,True]])
print(a>=2)
print(a.mean())
print(a[a>a.mean()])
print(a[~(a>a.mean())])
print(a[(a==0)|(a==1)])
print(a[(a<=2) & (a%2==0)])

A=np.random.randint(100,size=(3,3))
print(A)
print(A[np.array([
    [True,False,True],
    [False,True,False],
    [True,False,True]
])])
print(A>30)
print(A[A>30])

print("--------linear alzebra-------")
A=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
B=np.array([
    [6,5],
    [4,3],
    [2,1]
])
print(A.dot(B))
print(A@B)
print(B.T)
print(A)
print(B.T@A)

print("\n++++++useful numpy function++++++")
print("\nRandom")
print(np.random.random(size=2))
print(np.random.normal(size=2))
print(np.random.rand(2,4))
print("\narange")
print(np.arange(10))
print(np.arange(5,10))
print(np.arange(0,1,.1))
print("\nreshape")
print(np.arange(10).reshape(2,5))
print("\nlinspace")
print(np.linspace(0,1,5))
print(np.linspace(0,1,20))
print(np.linspace(0,1,20,False))
print("\nzeros,ones,empty")
print(np.zeros(5))
print(np.zeros((3,3)))
print(np.zeros((3,3),dtype=np.int8))
print(np.ones(5))
print(np.ones((3,3)))
print(np.empty(5))
print(np.empty((2,2)))