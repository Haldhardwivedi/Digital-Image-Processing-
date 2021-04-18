import cmath 
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
    # print("Inbuilt DFT of image : ",np.fft.fft2(result))
    return result3.T

def Magnitude(matrix):
    mag=[]
    mag2=[]
    li1=[]
    li2=[]
    for i in range(0,matrix.shape[0]):
        li1=[]
        li2=[]
        for j in range(0,matrix.shape[1]):
            li2.append(abs(matrix[i][j]))
            li1.append(((matrix[i][j].real)*(matrix[i][j].real) + (matrix[i][j].imag)*(matrix[i][j].imag))**0.5)
        mag.append(li1)
        mag2.append(li2)
    mag=np.array(mag)
    mag2=np.array(mag2)
    # print(mag)
    return mag

def Phase(matrix):
    phase=[]
    li=[]
    for i in range(0,matrix.shape[0]):
        li=[]
        for j in range(0,matrix.shape[1]):
            li.append((cmath.phase(matrix[i][j])))
        phase.append(li)
    phase=np.array(phase)
    # print("phase is : ",phase)
    return phase

def IDFT(signal):
    F=[]
    M=len(signal)
    for u in range(0,M):
        temp=0
        for x in range(0,M):
            temp+=(signal[x]*(np.exp((2j)*np.pi*u*x/M)))
        F.append(temp)
    return(F)

def FIND_IDFT(img):
    idft_result = IDFT(img)
    idft_real=[]
    for item in idft_result:
        idft_real.append(item.real)
    print("inbuilt",np.fft.ifft(img))
    return idft_real

def ORIGINAL(img):
    row=[]
    col=[]
    m,n=img.shape
    result = np.array(img)
    for p in result:
        row.append(FIND_IDFT(p))
    result2 = np.array(row)
    for p in result2.T:
        col.append(FIND_IDFT(p))
    result3 = np.array(col)
    return (result3.T/(m*n))

if __name__ == "__main__":
    img1 = cv2.imread("dog.tif", cv2.IMREAD_GRAYSCALE)
    img1 = cv2.resize(img1, (128,128), interpolation = cv2.INTER_AREA)
    img2 = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)
    img2 = cv2.resize(img2, (128,128), interpolation = cv2.INTER_AREA)
    
    # print("User defined DFT of image :  ",FFT_Image(img))

    fft_dog = FFT_Image(img1)
    fft_lena = FFT_Image(img2)

    print("Magnitude of Lena")
    print(Magnitude(fft_lena))

    print("Phase of Lena")
    print(Phase(fft_lena))

    print("Magnitude of Dog")
    print(Magnitude(fft_dog))

    print("Phase of Dog")
    print(Phase(fft_dog))
