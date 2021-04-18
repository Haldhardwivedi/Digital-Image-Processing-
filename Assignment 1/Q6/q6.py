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

def HistogramEqualization(img, cum_hist):
    #img is original grayscale image
    #cum_hist is cumulative histogram of original grayscale image
    width, height = img.shape
    
    cum_hist = cum_hist * 255 / (width*height)
    cum_hist = cum_hist.astype("uint8")

    newImg = np.zeros((width, height))

    for i in range(0, width):
        for j in range(0, height):
            newImg[i][j] = cum_hist[img[i][j]]

    return newImg
    #returns new image


if __name__=="__main__":
    OriginalGrayScale = cv.imread("Images/pout-dark.jpg", 0)

    # cv.imshow("Original", OriginalGrayScale)

    print(OriginalGrayScale.shape[1], OriginalGrayScale.shape[0])

    OriginalHistogram, OriginalCumulativeHistogram = HistogramCalculation(OriginalGrayScale)
    cv.imwrite("q6_Original_Gray_Scale.jpg", OriginalGrayScale)
    #print(OriginalHistogram)
    #print(OriginalCumulativeHistogram)

    NewGrayScale = HistogramEqualization(OriginalGrayScale, OriginalCumulativeHistogram)
    cv.imwrite("q6_New_Gray_Scale.jpg", NewGrayScale)
    NewGrayScale = NewGrayScale.astype('uint8')
    print(NewGrayScale.shape[1], NewGrayScale.shape[0])
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    #Plotting Original Histogram
    plt.figure()
    plt.title("Original Grayscale Histogram")
    plt.xlabel("Intensity level")
    plt.ylabel("Intensity Frequency")
    plt.xlim([0, 256])
    plt.plot(OriginalHistogram)
    plt.savefig("q6_Original_Grayscale_Histogram.jpg")

    #Plotting Original Cumulative Histogram
    plt.figure()
    plt.title("Original Grayscale Cumulative Histogram")
    plt.xlabel("Intensity level")
    plt.ylabel("Intensity Frequency")
    plt.xlim([0, 256])
    plt.plot(OriginalCumulativeHistogram)
    plt.savefig("q6_Original_Grayscale_Cumulative_Histogram.jpg")

    print(OriginalGrayScale.dtype)
    print(NewGrayScale.dtype)

    NewHistogram, NewCumulativeHistogram = HistogramCalculation(NewGrayScale)
    
    #Plotting New Histogram
    plt.figure()
    plt.title("New Grayscale Histogram")
    plt.xlabel("Intensity level")
    plt.ylabel("Intensity Frequency")
    plt.xlim([0, 256])
    plt.plot(NewHistogram)
    plt.savefig("q6_New_Grayscale_Histogram.jpg")

    #Plotting New Cumulative Histogram
    plt.figure()
    plt.title("New Grayscale Cumulative Histogram")
    plt.xlabel("Intensity level")
    plt.ylabel("Intensity Frequency")
    plt.xlim([0, 256])
    plt.plot(NewCumulativeHistogram)
    plt.savefig("q6_New_Grayscale_Cumulative_Histogram.jpg")
