#author__thea_uy
#date_april_21_2024

#this program will read text file nnamed numbers.txt taht contains 20 integers
#this program will also create two text file;
#thhis first text file will be named even.txt that will contain all even numbers extracted from numbers.txt
#the second text file will be named odd.txt that will contain all odd numbers extracted from numbers.txt

#list variables
even_list = []
odd_list= []

#read the text file numbers.txt
with open ("numbers.txt") as my_file:

#read every line of the text file numbers.txt & convert string to integer
    for number in my_file:
        numbers = int(number)

#determine if the numbers are even or odd
        if numbers % 2 == 0:
            even_list.append(numbers)
        elif numbers % 2 != 0:
            odd_list.append(numbers)

#create a new text file for even numbers


#create a new text file for odd numbers


#this is the end of the program