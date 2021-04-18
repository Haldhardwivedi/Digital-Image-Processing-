import cv2
import numpy as np 
import matplotlib.pyplot as plt
import array

def DFT(signal):
    F=[]
    M=len(signal)
    for u in range(0,M):
        temp=0
        for x in range(0,M):
            temp+=signal[x]*(np.exp((-2j)*np.pi*u*x/M))
        F.append(temp)
    return(F)

def FFT(f):
    M=len(f)
    odd=[]
    even=[]
    G=[]
    H=[]
    if M==1:
        return(DFT(f))
    else:
       for i in range(M):
        if i%2==0:
            even.append(f[i])
        else:
            odd.append(f[i])
       G=(DFT(even)).copy()
       H=(DFT(odd)).copy()
       F1=[]
       F2=[]
       for u in range(0,int(M/2)):
           temp1=G[u]+np.multiply(np.exp(-2j*np.pi*u/M),H[u])
           F1.append(temp1)
       for u in range(int(M/2),M):
           temp2=G[u-int(M/2)]-np.multiply(np.exp(-2j*np.pi*(u-int(M/2))/M),H[u-int(M/2)])
           F1.append(temp2)   
       return(F1)

def FFT_Image(img):
    row=[]
    col=[]
    result = np.array(img)
    for p in result:
        row.append(FFT(p))
    result2 = np.array(row)

    for p in result2.T:
        col.append(FFT(p))
    result3 = np.array(col)
    print("Inbuilt DFT of image : ",np.fft.fft2(result))
    return result3.T

if __name__=="__main__":
    img = cv2.imread("dog.tif", cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128,128), interpolation = cv2.INTER_AREA)
    print("User defined DFT of image :  ",FFT_Image(img))