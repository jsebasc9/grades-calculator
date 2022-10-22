
#Initialization of variables and lists
list_names = []
list_values = []
list_total_marks_students = []
list_total_marks_class = []
num_students = 0
top_class_mark = 0
num_assessments = 0
input_user_value = 0
mark = 0
input_user_name = ''
name_student = ''

#Function to calculate Grades depending of the marks
def calculate_grade(mark):
    
    if mark >= 80 and mark <= 100:
        grade = '(High Distinction).'
    elif mark >= 70 and mark <= 79:
        grade = '(Distinction).'
    elif mark >= 60 and mark <= 69:
        grade = '(Credit).'
    elif mark >= 50 and mark <= 59:
        grade = '(Pass).'
    elif mark >= 0 and mark <= 49:
        grade = '(Fail).'
    return grade

#Requesting number of assessments from the user, using exceptions to handle invalid entries
while num_assessments < 1:
    try:
        num_assessments = int(input('How many assessments?: '))
        if num_assessments < 1:
                print('Error : Entry of assessment have to be at least 1, try again . . .')
    except ValueError:
            print('Error : Invalid Input, try again . . .')

#Requesting name and value of assessments from the user handling exceptions    
for assessment in range(1, num_assessments + 1):
    while len(input_user_name) == 0:
        try:
            #Prompt for name of assessment
            print('Enter name of assessment', assessment, end=': ')
            input_user_name = input()   
            if len(input_user_name) == 0:
                raise ValueError('Error : Invalid Input, try again . . .')
        except ValueError as error:
            print(error)
    #Adding name of assessment to list_names
    list_names.append(input_user_name)

    
    #Handling exception while input user value would be less than 1
    while input_user_value < 1:
        try:
            #Prompt for marks of the assessment
            print('How many marks is the', input_user_name, end=' worth?: ')
            #Converting the entry to integer
            input_user_value = int(input())
            if input_user_value < 1:
                print('Error : value of assessment have to be at least 1, try again . . .')
        except ValueError:
            print('Error : Invalid Input, try again . . .')
    #Adding input of the user the list of values of assessments
    list_values.append(input_user_value)
    #Reseting input user for next iteration
    input_user_value = 0
    #Resseting input user name for next iteration
    input_user_name = ''
#Adding up list of values of the assessments to check total
total_sum_values = sum(list_values)


#Checking if sum of assessment values is not 100 to display an error and finish the program
if total_sum_values != 100:
    print('Error : value of assessments dont sum up 100, closing program')
else:
    #Because sum of assessment values is 100 the program can continue
    #Requesting number of students handling exceptions for invalid entries
    while num_students < 1:
        try:
            num_students = int(input('\nHow many students?: '))
            if num_students < 1:
                print('Error : Number of students have to be at least 1, try again . . .')
        except ValueError:
            print('Error : Invalid Input, try again . . .')
            

    #Starting loop for students stage and calculation of grades
    for student in range(1, num_students + 1):
        #Requesting name of student to append in the list handling exceptions for invalid inputs
        while len(name_student) == 0:
            try:
                print('\nWhat is the name of student', student, end=': ')
                name_student = input()   
                if len(name_student) == 0:
                    raise ValueError('Error : Invalid Input, try again . . .')
            except ValueError as error:
                print(error)
        

        #Requesting grade of the value of each assessment to calculate grade
        for value in range(len(list_values)):
            #Handling exceptions if the input is a valid entry and if is 0
            while True:
                #Display message and use of rstrip() to delete right space in value of list_names
                print('What did', name_student, 'get out of', list_values[value], 'in the',list_names[value].rstrip(),end='?  ')
                input_user_mark = input()
                try:
                    #If the user press only enter the mark will be 0
                    if len(input_user_mark) == 0:
                        mark = 0
                        break
                    else:
                        #Setting mark from the user entry
                        mark = int(input_user_mark)
                        break
                except ValueError:
                    print('Error : Invalid Input, try again . . .')
                    continue


            #If the user enters a mark superior thank the assessment, it will change the mark to the maximum of the assessment.
            if mark > list_values[value]:
                mark = list_values[value]
            #If the user enters a mark below 0, it will be set to 0
            elif mark < 0:
                mark = 0
            #Converting the corresponding marks for the function calculate grades
            mark_converted = mark/list_values[value]*100
            #Adding mark to list of total marks of the student
            list_total_marks_students.append(mark)
            #Calling the function to calculate grades and setting grade
            grade = calculate_grade(mark_converted)
            print(mark, ' out of' , list_values[value], 'is a' , grade )

            
        #Caculating average mark of the student depending of sum of marks and divided in the lenght
        total_mark = sum(list_total_marks_students)
        #Calling the function to calculate total grade
        grade = calculate_grade(total_mark)
        print(name_student, 'has a total mark of' , int(total_mark), grade,)
        #Adding mark to list of total marks of the class 
        list_total_marks_class.append(total_mark)
        #Checking and looking for the top student and setting name with mark
        if total_mark >= top_class_mark:
            top_student_name = name_student
            top_class_mark = int(total_mark)
        #Cleaning list of variables and total marks students for the next iteration
        list_total_marks_students.clear()
        name_student = ''
        mark = 0

    #Finalizing program printing final information and calculation class average and top student
    print('\nAll marks entered!')
    class_mark = sum(list_total_marks_class)/len(list_total_marks_class)
    grade = calculate_grade(class_mark)
    print('The class average is' ,round(class_mark), grade )
    #Use of rstrip() to delete right space in top_class_mark
    print('The top student is', top_student_name, 'with a total mark of', top_class_mark,end='.')

#Ending the program waiting for the user to press any key
end = input('\nPress any key to end the program . . .')
