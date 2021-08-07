#Initialization of variables and lists
list_names = []
list_values = []
index = 0
num_assessments = int(input('Please type number of assessments: '))

#Loop that repeats num_assessments times to fill a list with the names of assessments
print('Please type names of assessments')
while index < num_assessments:
    inputuser = input()
    list_names.append(inputuser)
    index += 1
print(list_names)
index = 0

#Loop that repeats num_assessments times to fill a list with the values of assessments
print('Please values of assessments')
while index < num_assessments:
    input_user = int(input())
    list_values.append(input_user)
    index += 1
print(list_values)
index = 0