#author__thea_uy
#date_april_21_2024

#this program will read a file containing the name of the 20 students together with their GWA
#this program will also display the name and GWA of the student/s who got the highest GWA


#import modules for display purposes
import pyfiglet

#list variables
student_name = []
student_grade = []
class_list = []

#read text file classlist.txt 
with open ("classlist.txt") as my_file:

#read every line of the text file classlist.txt
    for student in my_file:

#extract the full name of the students
        student_full_name = student[:-4]
        student_name.append(student_full_name)

#extract the grades of the students
        student_grades = student[-4:]
        student_grades = int(student_grades)
        student_grade.append(student_grades)

#determine the highest grade among the 20 students


#join the the lists containing the full name of the students and the grade of the students


#display message for the students


#determine which student/s got the highest grade


#display the sstudent/s who got the highest grade


#this is the end of the program