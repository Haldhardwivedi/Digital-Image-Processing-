import numpy as np 
import cv2 as cv
import math

# x1, y1, x2, y2 >= 0
def bilinear_interpolation(img, x1, y1, x2, y2, x, y):
    if x1 < 0 or y1 < 0 or x2 >= img.shape[0] or y2 >= img.shape[1]:
        return 0
    else:
        A1 = (x - x1) * (y - y1)
        A2 = (x - x1) * (y2 - y)
        A3 = (x2 - x) * (y - y1)
        A4 = (x2 - x) * (y2 - y)
        A = (x2 - x1) * (y2 - y1)
        res = img[x1][y1] * A4 + img[x1][y2] * A3 + img[x2][y1] * A2 + img[x2][y2]
        return res/A

def rotate_coordinates(x, y, theta, ox, oy):
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    x_n = (x - ox) * cos_theta - (y - oy) * sin_theta + ox
    y_n = (x - ox) * sin_theta + (y - oy) * cos_theta + oy
    return (int(x_n), int(y_n))

def inv_rotate_coordinates(x, y, theta, ox, oy):
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    x_n = (x - ox) * cos_theta + (y - oy) * sin_theta + ox
    y_n = (-x + ox) * sin_theta + (y - oy) * cos_theta + oy
    return (int(x_n), int(y_n))

def rotate_image_bi(img, theta, ox, oy):
    
    theta = theta * math.pi / 180
    width, height = img.shape
    # new_image = np.zeros((width, height), dtype="uint8")
    new_image = np.full((width, height),0, dtype="uint8")

    print(new_image)
    cv.imshow("bistart", new_image)

    for i in range(0,width):
        for j in range(0,height):
            x_n, y_n = rotate_coordinates(i, j, theta, ox, oy)
            # print("x and y : ", i,",",j," ---> ", "x_n and y_n : ",x_n, ",", y_n)
            if x_n >= 0 and x_n < width and y_n >= 0 and y_n < height:
                new_image[x_n][y_n] = img[i][j]

    cv.imshow("bimiddle", new_image)

    #bilinear interpolation
    for i in range(0,width):
        for j in range(0,height):
            if new_image[i][j] == 0:
                x_n, y_n = inv_rotate_coordinates(i, j, theta, ox, oy)
                x1 = math.floor(x_n)
                x2 = x1 + 1
                y1 = math.floor(y_n)
                y2 = y1 + 1
                new_image[i][j] = bilinear_interpolation(img, x1,y1, x2, y2, x_n, y_n)

    cv.imshow("bi", new_image)    

if __name__=="__main__":
    OriginalGrayScale = cv.imread("leaning_tower_of_pisa.jpg", 0)

    # #resizing
    # scale = 0.28
    width = int(OriginalGrayScale.shape[1])
    height = int(OriginalGrayScale.shape[0])
    # dimension = (width, height)

    # NewGrayScale = cv.resize(OriginalGrayScale, dimension, interpolation=cv.INTER_AREA)
    # cv.imwrite("leaning_tower_of_pisa.jpg", NewGrayScale)

    # print(OriginalGrayScale.shape)
    # print(NewGrayScale.shape)

    # cv.imshow("ltop", NewGrayScale)

    # blurred = cv.GaussianBlur(OriginalGrayScale, (3,3), 0)
    # horizontal_filter = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]

    # Calcution of Sobelx 
    # sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5) 

    # canny = cv.Canny(blurred, 225, 250)

    # cv.imshow("ltop", canny)

    rotate_image_bi(OriginalGrayScale, 5.5, width//2, height//2)

    cv.waitKey(0)
    cv.destroyAllWindows()
