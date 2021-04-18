import numpy as np
import userfunc as uf #contains user defined functions 

if __name__ == "__main__":
    m=5
    n=5
    matrix=np.zeros((m,n),dtype=np.int64)
    for i in range(0,m):
        for j in range(0,n):
            x=int(input())
            matrix[i][j]=x
    print("sum is : "+    str(uf.mxtrix_sum(matrix,m,n)))
    print("mean is : " +  str(uf.mean(matrix,m,n)))
    print("median is : "+ str(uf.median(matrix,m,n)))
    if uf.mode(matrix,m,n) !=-1 :
        print("mode is "+str(uf.mode(matrix,m,n)))
    print("Frequency distribution is :")
    uf.frequency(matrix,m,n)
    print("Standard Deviation is :"+ str(uf.standard_deviation(matrix,m,n)))
