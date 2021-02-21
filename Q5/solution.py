import numpy as np 
import cv2
import math

# builtin function to compare
def rotate_image_builtin(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

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
        res = img[x1][y1] * A4 + img[x1][y2] * A3 + img[x2][y1] * A2 + img[x2][y2] * A1
        return res/A

# returns coordinates in rotated space
def rotate_coordinates(x, y, theta, ox, oy):
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    x_n = (x - ox) * cos_theta - (y - oy) * sin_theta + ox
    y_n = (x - ox) * sin_theta + (y - oy) * cos_theta + oy
    return (int(x_n), int(y_n))

# inverse rotate transform
def inv_rotate_coordinates(x, y, theta, ox, oy):
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    x_n = (x - ox) * cos_theta + (y - oy) * sin_theta + ox
    y_n = (-x + ox) * sin_theta + (y - oy) * cos_theta + oy
    return (int(x_n), int(y_n))

def rotate_image_bi(img, theta, ox, oy):
    theta = theta * math.pi / 180
    width, height = img.shape
    new_image = np.full((width, height),0, dtype="uint8")
    for i in range(0,width):
        for j in range(0,height):
            x_n, y_n = rotate_coordinates(i, j, theta, ox, oy)
            if x_n >= 0 and x_n < width and y_n >= 0 and y_n < height:
                new_image[x_n][y_n] = img[i][j]

    if(theta % 2 == 0):
        cv2.imwrite("Uninterpolated_rotated"+str(theta)+".jpg", new_image)

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
    cv2.imshow("Rotated image", new_image)

if __name__=="__main__":
    OriginalGrayScale = cv2.imread("leaning_tower_of_pisa.jpg", 0)
    cv2.imshow("old", OriginalGrayScale)
    width = int(OriginalGrayScale.shape[1])
    height = int(OriginalGrayScale.shape[0])
    i = 0
    while(i < 8):
        rotate_image_bi(OriginalGrayScale, i, width//2, height//2)
        builtin_rotate_img = rotate_image_builtin(OriginalGrayScale, i)
        cv2.imshow("Builtin rotated image", builtin_rotate_img)
        cv2.waitKey(1)
        i += 1

    cv2.destroyAllWindows()
