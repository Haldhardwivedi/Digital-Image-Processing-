import cv2
import matplotlib.pylab as plt
import numpy as np
import math

# builtin function to return the rotated image
def get_rotated_image_builtin(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

# returns the transformed vector in the rotated image space
def get_transformed_vector(center, theta, vector):
  x1 = vector[0] - center[0]
  y1 = vector[1] - center[1]
  vector_transformed = np.array([
    (y1*math.sin(theta)) - (x1*math.cos(theta)),
    (y1*math.cos(theta)) + (x1*math.sin(theta))
  ])
  vector_transformed[0] = int(center[0] + vector_transformed[0])
  vector_transformed[1] = int(center[1] + vector_transformed[1])
  return vector_transformed

# returns the version of IMAGE rotated by angle THETA
def get_rotated_image(image, theta):
  new_img = np.zeros(image.shape, dtype=np.uint8)
  center = tuple(np.array(image.shape[1::-1]) / 2)
  for i in range(image.shape[0]):
    for j in range(image.shape[1]):
      vector_t = get_transformed_vector(center, theta, (i,j))
      new_img[vector_t[0]][vector_t[1]] = image[i][j]
  return new_img

# main function
def main():
  # filename = input("Enter the image file name: ")
  filename = "pisa.jpg"
  img = cv2.imread(filename, 1)
  new_img = get_rotated_image(img, 30)
  plt.imshow(new_img)
  plt.show()


if __name__=="__main__":
  main() 
