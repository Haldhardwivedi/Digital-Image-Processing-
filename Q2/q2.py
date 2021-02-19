import numpy as np
import random 
import userfunc as uf #contains user defined functions 

if __name__ == "__main__":
    m=int(input("row "))
    n=int(input("column "))
    matrix=np.random.randint(10, size=(m, n))
    print("Generated Matrix is : ")
    print(matrix)
    print("sum is : "+    str(uf.mxtrix_sum(matrix,m,n)))
    print("mean is : " +  str(uf.mean(matrix,m,n)))
    print("median is : "+ str(uf.median(matrix,m,n)))
    if uf.mode(matrix,m,n) !=-1 :
        print("mode is "+str(uf.mode(matrix,m,n)))
    uf.frequency(matrix,m,n)

