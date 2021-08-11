#Step 6 Completed. Starting Additions and Enhancements.

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

while num_assessments < 1:
    num_assessments = int(input('Please type number of assessments: '))
    if num_assessments < 1:
        print('Error : Number of assessment is less than 1')

for assessment in range(num_assessments):
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

if total_sum_values != 100:
    print('Error : value of assessments dont sum up 100, closing program')
else:
    #Restarting Index in the lists
    while num_students < 1:
        num_students = int(input('\nPlease type number of students : '))
        if num_students < 1:
            print('Error : Number of students is less than 1')
            #Starting students stage and calculation of grades

    for student in range(num_students):
        print('\nType name of student', student, end=' : ')
        name_student = input()

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
            grade = calculate_grade(mark_converted)
            print(mark, ' out of' , list_values[value], 'is' , grade )
            value += 1
        total_mark = sum(list_total_marks_students)/len(list_total_marks_students)
        grade = calculate_grade(total_mark)
        print(name_student, ' has a total mark of' , int(total_mark), '(' , grade, ')' )
        list_total_marks_class.append(total_mark)
        if total_mark > top_class_mark:
            top_student_name = name_student
            top_class_mark = total_mark
            
        list_total_marks_students.clear()

    print('\nAll Marks entered !')
    class_mark = sum(list_total_marks_class)/len(list_total_marks_class)
    grade = calculate_grade(class_mark)
    print('The class average is' , grade )
    print('The top student is ', top_student_name, 'with a total mark of ', int(top_class_mark))

