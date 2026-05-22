# inscribed midpoint polygons
# shape should be of this form: [(0,0), (1,0), (1,1), (0,1)]

import matplotlib.pyplot as plt
import math as math

rounding_number = 4

def midpoint_inscription(input_shape: list[tuple[float,float]]) -> list[tuple[float,float]]:
    
    inscribed_shape = []
    
    for i in range(len(input_shape) - 1):
        inscribed_shape.append(((input_shape[i][0] + input_shape[i+1][0])/2, (input_shape[i][1] + input_shape[i+1][1])/2))
    
    inscribed_shape.append(((input_shape[0][0] + input_shape[len(input_shape) - 1][0])/2, (input_shape[0][1] + input_shape[len(input_shape) - 1][1])/2))
    
    return inscribed_shape

def points_to_table(input_shape: list[tuple[float,float]]) -> list[list[float]]:

    x = []
    y = []

    for point in input_shape:
        x.append(point[0])
        y.append(point[1])
    
    x.append(input_shape[0][0])
    y.append(input_shape[0][1])

    return [x,y]

def midpoint_inscription_ntimes(input_shape: list[tuple[float,float]], n: int) -> list[tuple[float,float]]:
    
    plt.plot(points_to_table(input_shape)[0], points_to_table(input_shape)[1], marker='.')
    current = input_shape
    
    
    for j in range(n):
        current= midpoint_inscription(current)
        print(current)
        plt.plot(points_to_table(current)[0], points_to_table(current)[1], marker='.')

    plt.show()
    return(current)

def lists_rounded_equal_w_cycle(list1: list[float], list2: list[float]) -> bool:

    if len(list1) != len(list2):
        return False
    
    list1rounded = []
    list2rounded = []

    for i in range(len(list1)):
        list1rounded.append(round(list1[i], rounding_number))
        list2rounded.append(round(list2[i], rounding_number))
    
    str1 = ''.join(map(str, list1rounded))
    str2 = ''.join(map(str, list2rounded))

    return str2 in (str1 + str1)

def get_distance(input1: tuple[float,float], input2: tuple[float,float]):
    return (((input2[0] - input1[0]) ** 2) + ((input2[1] - input1[1]) ** 2)) ** 0.5


def shapes_are_similar(input1: list[tuple[float,float]], input2: list[tuple[float,float]]) -> bool:

    if len(input1) != len(input2):
        return False

    e_input1 = input1 + [input1[0], input1[1]]
    #print(e_input1)

    e_input2 = input2 + [input2[0], input2[1]]
    #print(e_input2)

    side_ratios1 = []
    side_ratios2 = []

    for i in range(len(input1)):

        first_side_length1 = get_distance(e_input1[0], e_input1[1])
        current_side_length1 = get_distance(e_input1[i], e_input1[i+1])

        first_side_length2 = get_distance(e_input2[0], e_input2[1])
        current_side_length2 = get_distance(e_input2[i], e_input2[i+1])

        side_ratios1.append(first_side_length1 / current_side_length1) 
        side_ratios2.append(first_side_length2 / current_side_length2) 
        

    angles1 = []
    angles2 = []

    for i in range(len(input1)):
       
       ab1 = get_distance(e_input1[i], e_input1[i+1])
       bc1 = get_distance(e_input1[i+1], e_input1[i+2])
       ca1 = get_distance(e_input1[i+2], e_input1[i])

       cosx1 = ((ab1 ** 2) + (bc1 ** 2) - (ca1 ** 2)) / (2 * ab1 * ca1)

       ab2 = get_distance(e_input1[i], e_input1[i+1])
       bc2 = get_distance(e_input1[i+1], e_input1[i+2])
       ca2 = get_distance(e_input1[i+2], e_input1[i])

       cosx2 = ((ab2 ** 2) + (bc2 ** 2) - (ca2 ** 2)) / (2 * ab2 * ca2)

       angles1.append(math.acos(cosx1))
       angles2.append(math.acos(cosx2))

    return lists_rounded_equal_w_cycle(side_ratios1, side_ratios2) and lists_rounded_equal_w_cycle(angles1, angles2)





square = [(0,0), (1,0), (1,1), (0,1)]

#print(midpoint_inscription_ntimes(square, 5))

triangle = [(5,6), (12, 32), (34, 124)]

print(shapes_are_similar(triangle, midpoint_inscription_ntimes(triangle,1)))

#new = midpoint_inscription(square)

#square_transformed = points_to_table(square)
#new_transformed = points_to_table(new)

#plt.plot(new_transformed[0], new_transformed[1], marker='o')
#plt.plot(square_transformed[0], square_transformed[1], marker='o')
          
#plt.show()