#author_thea_uy
#april_21_2024

#this program will create two separate text files after reading the source text file named integers.txt that contains 20 integers
#the first output file will be named double.txt containing the square of all even integers found in integers.txt
#the second file will be named triple.txt containing the sube of all odd numbers found in the integers.txt

#import modules
import math

#list variables
even_list = []
square_list = []
odd_list = []
cube_list = []

#read the text file integers.txt
with open ("integers.txt") as my_file:

#read every line of the text file integers.txt and convert from string to integers
    for number in my_file:
        numbers = int(number)

#determine if the numbers are even or odd
        if numbers % 2 == 0:
            even_list.append(numbers)
        elif numbers % 2 != 0:
            odd_list.append(numbers)

#get the square value of the even numbers from integers.txt
for square in even_list:
    square = pow(square,2)
    square_list.append(square)

#get the cube value of the odd numbers from integers.txt
for cube in odd_list:
    cube = pow(cube,3)
    cube_list.append(cube)

#create a new text file for square numbers
with open ("double.txt","a") as square_file:
    square_file.write(str(square_list))

#create a new text file for cube numbers
with open ("triple.txt" , "a") as cube_file:
    cube_file.write(str(cube_list))

#this is the end of the program