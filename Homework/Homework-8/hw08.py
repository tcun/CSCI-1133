import copy

#If you're not sure how to start, look at the swap_red_blue and blur
#examples below.

#Problem A: Invert Colors
def invert(img_matrix):
    '''
    Purpose:
      Inverts the colors in an image by setting each color component to
      255 minus its original value.
    Input Parameter(s):
      A 3D matrix (list of lists of lists) representing an .bmp image
      Each element of the matrix represents one row of pixels in the image
      Each element of a row represents a single pixel in the image
      Each pixel is represented by a list of three numbers between 0 and 255
      in the order [red, green, blue]
    Return Value:
      A 3D matrix of the same dimensions, with the colors of each pixel inverted
    '''
    inverted_img_matrix = []
    for i in range(len(img_matrix)):
      rgbs =[]
      for j in range(len(img_matrix[i])):
        rgb = []
        rgb.append((img_matrix[i][j][0] - 255) * -1)
        rgb.append((img_matrix[i][j][1] - 255) * -1)
        rgb.append((img_matrix[i][j][2] - 255) * -1)
        rgbs.append(rgb)
      inverted_img_matrix.append(rgbs)
    return inverted_img_matrix

# print(invert([[[127, 127, 127], [0, 0, 0]],
# [[255, 255, 0], [50, 128, 255]],
# [[0, 0, 255], [0, 255, 0]],
# [[255, 0, 0], [255, 255, 255]]])
# )



#Problem B: Grayscale
def grayscale(img_matrix):
    '''
    Purpose:
      Converts each pixel to grayscale with the formula:
      avg = int((red + green + blue)/3)
      applied to all three color components (truncated down to integer)
    Input Parameter(s):
      (see invert)
    Return Value:
      A 3D matrix of the same dimensions, with the pixels converted to grayscale
    '''
    grayscale_img_matrix = []
    for i in range(len(img_matrix)):
      rgbs =[]
      for j in range(len(img_matrix[i])):
        rgb = []
        gray = (img_matrix[i][j][0] + img_matrix[i][j][1] + img_matrix[i][j][2]) // 3
        for k in range(len(img_matrix[i][j])):
          rgb.append(gray)
        rgbs.append(rgb)
      grayscale_img_matrix.append(rgbs)
    return grayscale_img_matrix

# print(grayscale([[[127, 127, 127], [0, 0, 0]],
# [[255, 255, 0], [50, 128, 255]],
# [[0, 0, 255], [0, 255, 0]],
# [[255, 0, 0], [255, 255, 255]]]))

#Problem C: Rotate
def rotate(img_matrix):
    '''
    Purpose:
      Rotates an image 180 degrees.
    Input Parameter(s):
      (see invert)
    Return Value:
      A 3D matrix of the same dimensions, rotated 180 degrees.
    '''
    rotated_img_matrix = copy.deepcopy(img_matrix)
    for i in range(len(rotated_img_matrix)):
      temp = rotated_img_matrix[i]
      rotated_img_matrix[i] = temp[::-1]
    return rotated_img_matrix[::-1]
    


#Problem D: Edge Detect
def edge_detect(img_matrix):
  '''
  Purpose:
    Mark pixels that are significantly brighter than their surroundings
    in order to crudely detect edges in the image.
  Input Parameter(s):
    (see invert)
  Return Value:
    A 3D matrix of the same dimensions, where each pixel that is
    at least 1.1 times brighter than the average of their surrounding
    four pixels replaced with a white pixel ([255, 255, 255]),
    and any other pixels replaced with a black pixel ([0, 0, 0])
  '''
    
  outlined_img_matrix = []
  blank_row = []
  # First row is blank
  for i in range(len(img_matrix[0])):
   blank_row.append([0,0,0])
  outlined_img_matrix.append(blank_row)
  # Cannot be first or last row 
  for i in range(1, len(img_matrix) - 1):
    row = []
    row.append([0,0,0])

    # Cannot be first or last index (0, n-1)
    for j in range(1, len(img_matrix[0]) - 1):
      blank_index = [0,0,0]
      # Find average red value
      for k in range(3):
        average = (img_matrix[i+1][j][k] + img_matrix[i-1][j][k] + img_matrix[i][j-1][k] + img_matrix[i][j+1][k]) // 4
        # If the current RGB index is greater than the average red value + 10
        if(img_matrix[i][j][k] > average + 10):
          blank_index[k] = 255
      row.append(blank_index)

    row.append([0,0,0])
    outlined_img_matrix.append(row)
    # Add last blank row
  outlined_img_matrix.append(blank_row)
  return outlined_img_matrix;
    
for i in edge_detect(
[[[47,198,255],[47,198,255],[47,198,255],[47,198,255],[47,198,255]],
 [[47,198,255],[47,198,255],[47,198,255],[47,198,255],[47,198,255]],
 [[47,198,255],[47,198,255],[47,198,255],[47,198,255],[47,198,255]],
 [[47,198,255],[47,198,255],[47,198,255],[131,38,79] ,[131,38,79] ],
 [[47,198,255],[131,38,79] ,[131,38,79] ,[131,38,79] ,[131,38,79] ],
 [[131,38,79] ,[131,38,79] ,[131,38,79] ,[131,38,79] ,[131,38,79] ],
 [[131,38,79] ,[131,38,79] ,[131,38,79] ,[131,38,79] ,[131,38,79] ],
 [[131,38,79] ,[131,38,79] ,[131,38,79] ,[131,38,79] ,[131,38,79] ]]):
  print(i)

#Example #1: Swapping red and blue components
def swap_red_blue(img_matrix):
    '''
    Purpose:
      Swaps the red and blue components in an image
    Input Parameter(s):
      (see invert)
    Return Value:
      A 3D matrix of the same dimensions, with all colors inverted
      (that is, for every pixel list, the first and last values have been
      swapped.
    '''
    height = len(img_matrix)  #Height = # of rows, i.e. length of matrix
    width = len(img_matrix[0]) #Width = # of columns, i.e. length of one row
    for y in range(height):
        for x in range(width):
            # img_matrix[y][x] is a 3-element list representing the
            # [red, green, blue] values for the pixel at coordinates (x, y)
            old_red = img_matrix[y][x][0]
            old_blue = img_matrix[y][x][2]
            img_matrix[y][x][0] = old_blue
            img_matrix[y][x][2] = old_red
    return img_matrix


#Example #2: Blur the image
#(this is a little more complex than the ones you need to do)
def blur(img_matrix):
    '''
    Purpose:
      Blurs an image by applying a 3x3 pixel filter
    Input Parameter(s):
      (see invert)
    Return Value:
      A 3D matrix of the same dimensions, with each pixel blurred:
      each color component is averaged with the surrounding 9 pixels
    '''
    height = len(img_matrix)
    width = len(img_matrix[0])
    #Make a deep copy of the matrix to use as our output matrix.
    #This is just a convenient way to get an output matrix of the same
    #dimensions as the original.
    new_matrix = copy.deepcopy(img_matrix)

    #Loops through every pixel we need to compute via (x, y) coordinates
    for y in range(height):
        for x in range(width):

            #To compute each pixel, for each of the three color components
            #take the average of that component for the surrounding 9 pixels
            new_pixel = [0, 0, 0]
            for j in range(-1,2):  #Loop through y-1, y, y+1
                for i in range(-1,2):  #Loop through x-1, x, x+1
                    for color in range(3):
                        #If x+i or y+j is out of bounds, ignore it
                        if 0 <= x+i < width and 0 <= y+j < height:
                            new_pixel[color] += img_matrix[y+j][x+i][color]/9

            #Averaging might result in a float, so truncate down to nearest int
            for color in range(3):
                new_pixel[color] = int(new_pixel[color])

            #Replace pixel in output matrix
            new_matrix[y][x] = new_pixel
    return new_matrix



#--------------------------------------------------
# DO NOT EDIT ANYTHING BELOW THIS LINE
# .bmp file manipulation functions.  You don't have to understand these.
#--------------------------------------------------

def big_end_to_int(ls):
    '''
    Byte conversion helper 
    Purpose:
      Compute the integer represented by a sequence of bytes
    Input Parameter(s):
      A list of bytes (integers between 0 and 255), in big-endian order
    Return Value:
      Integer value that the bytes represent
    '''
    total = 0
    for ele in ls[::-1]:
        total *= 256
        total += ele
    return total

def transform_image(fname,operation):
    '''
    .bmp conversion function
    Purpose:
      Turns a .bmp file into a matrix of pixel values, performs an operation
      on it, and then converts it back into a new .bmp file
    Input Parameter(s):
      fname, a string representing a file name in the current directory
      operation, a string representing the operation to be performed on the
      image.  This can be one of 6 options: 'invert', 'grayscale', 'rotate',
      or 'edge_detect'. TODO FIX THIS
    Return Value:
      None
    '''
    #Open file in read bytes mode, get bytes specifying width/height
    fp = open(fname,'rb')
    data = list(fp.read())
    old_data = list(data)
    width = big_end_to_int(data[18:22])
    height = big_end_to_int(data[22:26])

    #Data starts at byte 54.  Create matrix of pixels, where each
    #pixel is a 3 element list [red,green,blue].
    #Starts in lower left corner of image.
    i = 54
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = [data[i+2],data[i+1],data[i]]
            i += 3
            row.append(pixel)
        matrix.append(row)
        #Row size must be divisible by 4, otherwise padding occurs
        i += (2-i)%4
    fp.close()

    #Perform operation on the pixel matrix
    if operation == 'invert':
        new_matrix = invert(matrix[::-1])
    elif operation == 'grayscale':
        new_matrix = grayscale(matrix[::-1])
    elif operation == 'rotate':
        new_matrix = rotate(matrix[::-1])
    elif operation == 'edge_detect':
        new_matrix = edge_detect(matrix[::-1])
    elif operation == 'blur':
        new_matrix = blur(matrix[::-1])
    elif operation == 'swap_red_blue':
        new_matrix = swap_red_blue(matrix[::-1])
    else:
        return
    new_matrix = new_matrix[::-1]
    #Write back to new .bmp file.
    #New file name is operation+fname
    i = 54
    for y in range(height):
        for x in range(width):
            pixel = tuple(new_matrix[y][x])
            data[i+2],data[i+1],data[i] = pixel
            i += 3
        i += (2-i)%4
    fp = open(operation+"_"+fname,'wb')
    fp.write(bytearray(data))
    fp.close()

def to_hex(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            outstr = ''
            for color in range(3):
                outstr += hex(matrix[y][x][color])
            outstr = outstr.replace('0x','')
            matrix[y][x] = outstr
    return matrix

