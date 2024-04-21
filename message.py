#author__thea_uy
#date_april_21_2024

#this program will write multiple line of text contents into a text file mylife.txt

#initialize a loop
while True:

#variable for the input
    message = ""

#ask the user for the number of lines
    number_of_lines = int(input("Enter a value: "))

#let the user enter their message
    for lines in range(number_of_lines):
        message += input () + "\n"

#create a text file mylife.txt
    with open ("mylife.txt", "a") as message_file:
        message_file.write(message)

#ask the user if they want to try again
    answer = input("Do you want to try again? ")
    if answer == "yes":
        continue
    elif answer == "no":
        break

#this is the end of the program!