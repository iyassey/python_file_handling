#author__thea_uy
#date_april_21_2024

#this program will write multiple line of text contents into a text file mylife.txt

#initialize a loop
while True:

#variable for the input
    message = ""

#ask the user for the number of lines
    while True:
        try:
            number_of_lines = int(input("Enter the numbers of lines: "))
            if number_of_lines>0:
                break
            else:
                continue
        except ValueError:
            continue
    

#let the user enter their message
    for lines in range(number_of_lines):
        message += input () + "\n"

#ask the user to if they want to append or write
    while True:
        try:
            answer = str(input("Do you want to append or write? \nAppend lets add additional messsage \nWrite lets you overwrite the existing messsage: \na/w: "))
            answer = answer[:1].lower()

#create a text file mylife.txt - lets the user append the text file
            if answer == "a":
                with open ("mylife.txt", "a") as message_file:
                    message_file.write(message)
                    break

#create a text file mylife.txt - lets the user write the text file
            elif answer == "w":
                with open ("mylife.txt", "w") as message_file:
                    message_file.write(message)
                    break

#if the user type other answers that are not valid - the program will ask again the user for answer           
            else:
                continue
        except ValueError:
            continue



#ask the user if they want to try again
    while True:
        try:
            final_answer = str(input("Do you want to try again? yes or no: "))
            if final_answer == "yes":
                break
            elif final_answer == "no":
                print("Thank you for using my program!")
                exit()
            else:
                continue
        except ValueError:
            continue

#this is the end of the program!