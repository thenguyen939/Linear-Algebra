# Numerical linear algebra - Gauss Elimination
import numpy as np
# -----------------------------------------------
def to_upper_matrix(HS,KQ,n):
    A=HS.copy()
    b=KQ.copy()
    flag=1
    for i in range(n):
        if A[i,i]==0:
            j=i+1
            while j<n:
                if A[j,i]!=0: 
                    A= Doi(A,i,j,n)
                    break 
                j=j+1
            if j==n: 
                flag=0
                break
        pivot=A[i,i]
        for j in range(i+1,n):
            l=A[j,i]/A[i,i]
            b[j]=b[j]-l*b[i]
            for k in range(0,n):
                A[j,k]=A[j,k]-l*A[i,k]
    if flag==0:
        print("Khong khu duoc")
    else:
        return A,b
# ---------------------------------------------------------
def Doi(B,i,j,n):
    A=B.copy()
    for k in range(0,n):
        c = A[i,k]
        A[i,k]=A[j,k]
        A[j,k]=c
    return A
#----------------------------------------------------------
def nghiem(A,b,n):
    x=np.zeros(n)
    for k in range(n-1,-1,-1):
        sum =0 
        for j in range(k+1, n):
            sum = sum + A[k,j]*x[j]
        x[k]=(b[k]-sum)/A[k,k]
    return x
#----------------------------------------------------------
a=np.array([[1,2,3],[3,4,6],[3,2,1]])
b=np.array([1,2,3])
[ak,bk] =to_upper_matrix(a,b,3)
print(ak)
print(bk)
x= nghiem (ak,bk,3)
print(x)
print(a*x.T)
        


             

            

