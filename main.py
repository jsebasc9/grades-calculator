#Step 6 Completed. Starting Additions and Enhancements. Adding Handling Exceptions

#Initialization of variables and lists
list_names = []
list_values = []
list_total_marks_students = []
list_total_marks_class = []
num_students = 0
top_class_mark = 0
num_assessments = 0
input_user_value = 0

#Function to calculate Grades
def calculate_grade(mark):
    
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
    return grade

# while num_assessments < 1:
#     try:
#         num_assessments = int(input('Please type number of assessments: '))
#     except:
#         print('Error : Something went wrong, try again . . .')

#Requesting number of assessments from the user
while num_assessments < 1:
    num_assessments = int(input('Please type number of assessments: '))
    if num_assessments < 1:
        print('Error : Number of assessment is less than 1')

#Requesting name and value of assessments from the user       
for assessment in range(1, num_assessments + 1):
    print('Type name of assessment ', assessment, end=' : ')
    input_user_name = input()   
    list_names.append(input_user_name)
    while input_user_value < 1:
        input_user_value = int(input('Please put value of assessment : '))
        if input_user_value < 1:
            print('Error : value of assessment is less than 1')
    list_values.append(input_user_value)
    input_user_value = 0
    assessment += 1
total_sum_values = sum(list_values)

#Checking if sum of assessment values is not 100
if total_sum_values != 100:
    print('Error : value of assessments dont sum up 100, closing program')
else:
    #Because sum of assessment values is 100 the program can continue
    #Requesting number of students
    while num_students < 1:
        num_students = int(input('\nPlease type number of students : '))
        if num_students < 1:
            print('Error : Number of students is less than 1')
            
    #Starting students stage and calculation of grades
    for student in range(1, num_students + 1):
        #Requesting name of student to append in the list
        print('\nType name of student', student, end=' : ')
        name_student = input()
        #Requesting grade of the value of each assessment to calculate grade
        for value in range(len(list_values)):
            print('What did ', name_student, 'get out of', list_values[value], ' in the ',list_names[value], '? ', end=' : ')
            mark = int(input())
            #If the user enters a mark superior thank the assessment, it will change the mark to the maximum of the assessment.
            if mark > list_values[value]:
                mark = list_values[value]
            #If the user enters a mark below 0, it will be set to 0
            elif mark < 0:
                mark = 0
            mark_converted = mark*100/list_values[value]
            list_total_marks_students.append(mark_converted)
            #Calling the function to calculate grades and setting grade
            grade = calculate_grade(mark_converted)
            print(mark, ' out of' , list_values[value], 'is' , grade )
            value += 1
        #Caculating average mark of the student depending of sum of marks and divided in the lenght
        total_mark = sum(list_total_marks_students)/len(list_total_marks_students)
        #Calling the function to calculate total grade
        grade = calculate_grade(total_mark)
        print(name_student, ' has a total mark of' , int(total_mark), '(' , grade, ')' )
        list_total_marks_class.append(total_mark)
        #Checking and looking for the top student and setting name with mark
        if total_mark > top_class_mark:
            top_student_name = name_student
            top_class_mark = total_mark
        #Cleaning list for the next iteration
        list_total_marks_students.clear()

    #Finilizing program printing final information and calculation class average and top student
    print('\nAll Marks entered !')
    class_mark = sum(list_total_marks_class)/len(list_total_marks_class)
    grade = calculate_grade(class_mark)
    print('The class average is' , grade )
    print('The top student is ', top_student_name, 'with a total mark of ', int(top_class_mark))

end = input('Press any key to end the program . . .')
