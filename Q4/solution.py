import cv2
import numpy

def get_value(a1, a2, x1, y1, x2, y2, arr):
  l = arr.shape;
  if(a1 > l[0] or x1 > l[0] or x2 > l[0] or a2 > l[1] or y1 > l[1] or y2 > l[1]):
    return 0
  return (arr[a1][a2] * (y2 - y1) * (x2 - x1))

def get_interpolated_value(i, j, arr, factor):
  if(arr[i][j][0] != 0 or arr[i][j][1] != 0 or arr[i][j][2] != 0):
    return arr[i][j]
  x1 = i; y1 = j 
  x2 = i; y2 = j; val = 0
  while(x1 % factor != 0):
    x1 -= 1
  while(y1 % factor != 0):
    y1 -= 1 
  x2 = x1 + factor; y2 = y1 + factor
  val += get_value(x2, y2, x1, y1, i, j); #A1
  val += get_value(x2, y1, x1, j, i, y2); #A2
  val += get_value(x1, y2, i, y1, x2, j); #A3
  val += get_value(x1, y1, i, j, x2, y2); #A4
  # val += arr[x2][y2] * get_area(x1, y1, i, j) #A1
  # val += arr[x2][y1] * get_area(x1, j, i, y2) #A2
  # val += arr[x1][y2] * get_area(i, y1, x2, j) #A3  
  # val += arr[x1][y1] * get_area(i, j, x2, y2) #A4  
  return val

# returns an array of appropriate shape
def get_new_arr(old_shape, factor):
  dim1 = int(old_shape[0]*factor)
  dim2 = int(old_shape[1]*factor)
  new_arr = numpy.zeros([dim1, dim2, 3], dtype=int)
  return new_arr

# returns the new image scaled by the FACTOR
def get_scaled_image(old_arr, factor):
  new_arr = get_new_arr(old_arr.shape, factor)
  for i in range(0, old_arr.shape[0] - 1):
    for j in range(0, old_arr.shape[1] - 1):
      i_new = int(i * factor)
      j_new = int(j * factor)
      new_arr[i_new][j_new] = old_arr[i][j]

  for i in range(0, new_arr.shape[0] - 1):  
    for i in range(0, new_arr.shape[1] - 1):
      new_arr[i][j] = get_interpolated_value(i, j, new_arr, factor)  

  return new_arr

# the main function 
def main(): 
  # filename = input("Enter the file name: ");
  factor = int(input("Enter the factor u want to scale: "))
  filename = "lena.jpg"
  # factor = 2
  old_arr = cv2.imread(filename, 1)
  new_arr = get_scaled_image(old_arr, factor)
  cv2.imwrite("lena factored.jpg", new_arr);
    
if __name__=="__main__": 
  main() 

