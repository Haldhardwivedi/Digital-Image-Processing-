import numpy as np 
import cv2 as cv
from matplotlib import pyplot as plt 

def HistogramCalculation(img):
    #img is original grayscale image
    width, height = img.shape
    hist = np.zeros(256, dtype='int32')
    cum_hist = np.zeros(256, dtype='int32')

    for i in range(0,width):
        for j in range(0,height):
            hist[img[i][j]] += 1

    cum_hist[0] = hist[0]
    for k in range(1,256):
        cum_hist[k] = hist[k] + cum_hist[k-1]

    return hist, cum_hist

def HistogramMatching(img, cum_hist, ref_cum_hist):
    #img is original grayscale image
    #cum_hist is cumulative histogram of original grayscale image
    #ref_cum_hist is cumulative histogram of reference grayscale image
    width, height = img.shape
    
    cum_hist = cum_hist * 255 / (width*height)
    cum_hist = cum_hist.astype("uint8")

    ref_cum_hist = ref_cum_hist * 255 / (width*height)
    ref_cum_hist = ref_cum_hist.astype("uint8")

    newImg = np.zeros((width, height))

    for i in range(0, width):
        for j in range(0, height):
            a = img[i][j]
            b = cum_hist[a]
            temp_ref_ch = ref_cum_hist - b
            temp_min_index = 0
            for k in range(1, 256):
                if abs(temp_ref_ch[k]) < abs(temp_ref_ch[temp_min_index]):
                    temp_min_index = k
            newImg[i][j] = temp_min_index
    
    newImg = newImg.astype("uint8")
    return newImg
    #returns new image


if __name__=="__main__":
    OriginalGrayScale = cv.imread("Images/pout-dark.jpg", 0)

    ReferenceGrayScale = cv.imread("Images/pout-bright.jpg", 0)

    # cv.imshow("Original", OriginalGrayScale)

    print(OriginalGrayScale.shape[1], OriginalGrayScale.shape[0])
    print(ReferenceGrayScale.shape[1], ReferenceGrayScale.shape[0])

    OriginalHistogram, OriginalCumulativeHistogram = HistogramCalculation(OriginalGrayScale)
    cv.imwrite("q7_Original_Gray_Scale.jpg", OriginalGrayScale)

    ReferenceHistogram, ReferenceCumulativeHistogram = HistogramCalculation(ReferenceGrayScale)
    cv.imwrite("q7_Reference_Gray_Scale.jpg", ReferenceGrayScale)
    #print(OriginalHistogram)
    #print(OriginalCumulativeHistogram)
    
    NewGrayScale = HistogramMatching(OriginalGrayScale, OriginalCumulativeHistogram, ReferenceCumulativeHistogram)
    NewHistogram, NewCumulativeHistogram = HistogramCalculation(NewGrayScale)
    cv.imwrite("q7_New_Gray_Scale.jpg", NewGrayScale)

    #Plotting Original Histogram
    plt.figure()
    plt.title("Original Grayscale Histogram")
    plt.xlabel("Intensity level")
    plt.ylabel("Intensity Frequency")
    plt.xlim([0, 256])
    plt.plot(OriginalHistogram)
    plt.savefig("q7_Original_Grayscale_Histogram.jpg")

    #Plotting Original Cumulative Histogram
    plt.figure()
    plt.title("Original Grayscale Cumulative Histogram")
    plt.xlabel("Intensity level")
    plt.ylabel("Intensity Frequency")
    plt.xlim([0, 256])
    plt.plot(OriginalCumulativeHistogram)
    plt.savefig("q7_Original_Grayscale_Cumulative_Histogram.jpg")

    print(OriginalGrayScale.dtype)
    print(ReferenceGrayScale.dtype)
    print(NewGrayScale.dtype)
    
    #Plotting Reference Histogram
    plt.figure()
    plt.title("Reference Grayscale Histogram")
    plt.xlabel("Intensity level")
    plt.ylabel("Intensity Frequency")
    plt.xlim([0, 256])
    plt.plot(ReferenceHistogram)
    plt.savefig("q7_Reference_Grayscale_Histogram.jpg")

    #Plotting Reference Cumulative Histogram
    plt.figure()
    plt.title("Reference Grayscale Cumulative Histogram")
    plt.xlabel("Intensity level")
    plt.ylabel("Intensity Frequency")
    plt.xlim([0, 256])
    plt.plot(ReferenceCumulativeHistogram)
    plt.savefig("q7_Reference_Grayscale_Cumulative_Histogram.jpg")

    #Plotting New Histogram
    plt.figure()
    plt.title("New Grayscale Histogram")
    plt.xlabel("Intensity level")
    plt.ylabel("Intensity Frequency")
    plt.xlim([0, 256])
    plt.plot(NewHistogram)
    plt.savefig("q7_New_Grayscale_Histogram.jpg")

    #Plotting New Cumulative Histogram
    plt.figure()
    plt.title("New Grayscale Cumulative Histogram")
    plt.xlabel("Intensity level")
    plt.ylabel("Intensity Frequency")
    plt.xlim([0, 256])
    plt.plot(NewCumulativeHistogram)
    plt.savefig("q7_New_Grayscale_Cumulative_Histogram.jpg")

   