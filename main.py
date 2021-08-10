#Working in Task 5.2

#Initialization of variables and lists
list_names = []
list_values = []
list_total_marks = []
sub_index = 0
num_students = 0

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

num_assessments = int(input('Please type number of assessments: '))

for assessment in range(num_assessments):       
    input_user = input('Type name of assessment : ')   
    list_names.append(input_user)
    input_user = int(input('Please put value of assessment : '))
    list_values.append(input_user)
    assessment += 1
total_sum_values = sum(list_values)

if total_sum_values != 100:
    print('Assessments dont sum up 100')
else:
    #Restarting Index in the lists
    num_students = int(input('Type number of students : '))
            #Starting students stage and calculation of grades

    for student in range(num_students):
        name_student = input('Type name of student : ')

        for sub_index in range(len(list_values)):
            print('What did ', name_student, 'get out of', list_values[sub_index], ' in the ',list_names[sub_index], '? : ')
            mark = int(input())
            #If the user enters a mark superior thank the assessment, it will change the mark to the maximum of the assessment.
            if mark > list_values[sub_index]:
                mark = list_values[sub_index]
            #If the user enters a mark below 0, it will be set to 0
            if mark < 0:
                mark = 0
            list_total_marks.append(mark)
            grade = calculate_grade(mark)
            print(mark, ' out of' , list_values[sub_index], 'is' , grade )
            sub_index += 1
        total_mark = sum(list_total_marks)/len(list_total_marks)
        grade = calculate_grade(total_mark)
        print(name_student, ' has a total mark of' , total_mark, '(' , grade, ')' )
        list_total_marks.clear()

