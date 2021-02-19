from collections import Counter 

def mxtrix_sum(matrix,m,n):
    val=0
    for i in range(0,m):
        for j in range(0,n):
            val=val+matrix[i][j]
    return val
def matrix_max(matrix,m,n):
    mxv =matrix[0][0]
    for i in range(0,m):
        for j in range(0,n ):
            if matrix[i][j]>mxv:
                mxv=matrix[i][j]
    
    return mxv

def mean(matrix,m,n):
    mval=mxtrix_sum(matrix,m,n)
    return mval/(m*n)

def median(matrix,m,n):
    n_num=[]
    for i in range(0,m):
        for j in range (0,n):
            n_num.append(matrix[i][j])
    n=len(n_num)
    n_num.sort() 
    median=0
    if n%2 == 0:
        median1 = n_num[n//2] 
        median2 = n_num[n//2 - 1] 
        median = (median1 + median2)/2
    else :
        median = n_num[n//2]
    return median

def mode(matrix,m,n):
    n_num=[]
    for i in range(0,m):
        for j in range(0,n):
            n_num.append(matrix[i][j])
    n=len(n_num)
    data=Counter(n_num)
    mode_val=dict(data)
    res = [k for k, v in mode_val.items() if v == max(list(data.values()))]
    if len(res) == n:
        print("No mode found ")
        return -1
    else:
        return (res)


def frequency(matrix,m,n):
    n_num=[]
    for i in range(0,m):
        for j in range(0,n):
            n_num.append(matrix[i][j])
    n=len(n_num)
    data=Counter(n_num)
    mode_val=dict(data)
    for k, v in mode_val.items() :
        print(str(k)+'->'+str(v))


            
