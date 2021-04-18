import cv2
import numpy

# returns the product of corner-intensity(a1, a2) and opposite area(x1, y1, x2, y2)
def get_value(a1, a2, x1, y1, x2, y2, arr):
  m1 = arr.shape[0] - 1;
  m2 = arr.shape[1] - 1;
  value_arr = numpy.array([0, 0, 0])
  if(a1>m1 or x1>m1 or x2>m1 or a2>m2 or y1>m2 or y2>m2):
    return value_arr
  value_arr[0] = arr[a1][a2][0] * (y2-y1) * (x2-x1)
  value_arr[1] = arr[a1][a2][1] * (y2-y1) * (x2-x1)
  value_arr[2] = arr[a1][a2][2] * (y2-y1) * (x2-x1)
  return value_arr

# returns the interpolated value of f'(i,j) based upon the corner values
def get_interpolated_value(i, j, arr, factor):
  if(arr[i][j][0] != 0 or arr[i][j][1] != 0 or arr[i][j][2] != 0):
    return arr[i][j]
  x1 = i; y1 = j 
  while(x1 % factor != 0):
    x1 -= 1
  while(y1 % factor != 0):
    y1 -= 1 
  x2 = int(((x1/factor)+1) * factor)
  y2 = int(((y1/factor)+1) * factor)
  total_area = (x2-x1) * (y2-y1)
  val1 = get_value(x2, y2, x1, y1, i, j, arr); #A1
  val2 = get_value(x2, y1, x1, j, i, y2, arr); #A2
  val3 = get_value(x1, y2, i, y1, x2, j, arr); #A3
  val4 = get_value(x1, y1, i, j, x2, y2, arr); #A4
  for q in range(3):
    val1[q] = (val1[q] + val2[q] + val3[q] + val4[q]) / total_area
  return val1

# returns an array of resized shape
def get_resized_arr(old_shape, factor):
  dim1 = int(old_shape[0]*factor)
  dim2 = int(old_shape[1]*factor)
  new_arr = numpy.zeros([dim1, dim2, 3], dtype=int)
  return new_arr

# returns the new image scaled by the FACTOR
def get_scaled_image(old_arr, factor):
  new_arr = get_resized_arr(old_arr.shape, factor)
  for i in range(old_arr.shape[0]):
    for j in range(old_arr.shape[1]):
      i_new = int(i * factor)
      j_new = int(j * factor)
      new_arr[i_new][j_new] = old_arr[i][j]

  for i in range(new_arr.shape[0]):  
    for j in range(new_arr.shape[1]):
      new_arr[i][j] = get_interpolated_value(i, j, new_arr, factor)  
  return new_arr

# the main function 
def main(): 
  filename = input("Enter the file name: ");
  # factor = float(input("Enter the factor u want to scale: "))
  filename = "lena.jpg"
  old_arr = cv2.imread(filename, 1)

  x = old_arr.shape[0]
  y = old_arr.shape[1]
  new_arr1 = get_scaled_image(old_arr, 0.5)
  new_arr2 = get_scaled_image(old_arr, 1)
  new_arr3 = get_scaled_image(old_arr, 2)
  builtin_half = cv2.resize(old_arr, (x//2, y//2))
  builtin_once = cv2.resize(old_arr, (x, y))
  builtin_twice = cv2.resize(old_arr, (2*x, 2*y))

  cv2.imwrite("lena_halffactored.jpg", new_arr1);
  cv2.imwrite("lena_oncefactored.jpg", new_arr2);
  cv2.imwrite("lena_twicefactored.jpg", new_arr3);
  cv2.imwrite("lena_builtin_halffactored.jpg", builtin_half);
  cv2.imwrite("lena_builtin_oncefactored.jpg", builtin_once);
  cv2.imwrite("lena_builtin_twicefactored.jpg", builtin_twice);


if __name__=="__main__": 
  main() 

