#Stargin STEP 4
#Initialization of variables and lists
import sys

list_names = []
list_values = []
index = 0
num_assessments = int(input('Please type number of assessments: '))

#Function to calculate Grades
def calculategrade(mark, value):
    if mark >= 80:
        grade = 'HD (High Distinction)'
    elif mark >= 70:
        grade = 'D (Distinction)'
    elif mark >= 60:
        grade = 'CR (Credit)'
    elif mark >= 50:
        grade = 'P (Pass)'  
    else:
        grade = 'F (Fail)'
    print(value, ' out of' , mark, 'is' , grade )


while True:
    #Checking if the number of assessments is greater than 1, also, if the lists are not full
    if index < num_assessments and num_assessments >= 1:  
        #Loop that repeats num_assessments times to fill a list with the names of assessments
        while index < num_assessments:
            
            input_user = input('Type name of assessment : ')
            #Checking if the assessment name is in the list
            if (input_user in list_names):
                print('The assessment is already in the list, please put a different name  : ')
                break
            else:    
                list_names.append(input_user)
                input_user = int(input('Please put value of assessment : '))
                list_values.append(input_user)
                index += 1
            
        print(list_names)
        print(list_values)
    #If the list are full the program ends    
    elif index != 0 and index == num_assessments:
        total_sum_values = sum(list_values)
        if total_sum_values == 100:
            #Restarting Index in the lists
            index = 0
            num_students = int(input('Type number of students : '))
            while index < num_students:
                name_student = input('Type name of student : ')
                print('What did ', name_student, 'get out of', list_values[index], ' in the essay? : ')
                mark = int(input())
                calculategrade(mark, list_values[index])
                index += 1

        else:
            print('The assessment values dont sum up to 100, the program will finish')
            break

    #If the user input less than 1 assessments the program asks for the number again.
    else:    
        num_assessments = int(input('Error: you have to put at least 1, please type number of assessments: '))

