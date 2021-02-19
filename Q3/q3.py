import  cv2 
import noise as nsz


img = cv2.imread('lena.jpg')
cv2.imshow('Lena image',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

img_gray = cv2.imread('lena.jpg',0)
cv2.imshow('Lena_Gray',img_gray)
cv2.waitKey(5000)
cv2.destroyAllWindows()

for x in range(6):
    temp = 0
    for y in range(5 * (x + 1)):
        noise_img = nsz.noisy("gauss",img)
        temp += noise_img
    cv2.imshow('Lena_Gray Gaussian' + str(x),temp/(5*(x + 1)))
cv2.waitKey(5000)
cv2.destroyAllWindows()

for x in range(6):
    temp = 0
    for y in range(5 * (x + 1)):
        noise_img = nsz.noisy("s&p",img)
        temp += noise_img
    cv2.imshow('Lena_Gray Salt and Pepper' + str(x),temp/(5*(x + 1)))
cv2.waitKey(5000)
cv2.destroyAllWindows()

for x in range(6):
    temp = 0
    for y in range(5 * (x + 1)):
        noise_img =nsz.noisy("speckle",img)
        temp += noise_img 
    cv2.imshow('Lena_Gray Speckle ' + str(x),temp/(5*(x + 1)))
cv2.waitKey(5000)
cv2.destroyAllWindows()
