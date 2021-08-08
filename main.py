#Initialization of variables and lists
list_names = []
list_values = []
index = 0
num_assessments = int(input('Please type number of assessments: '))

while(True):
    if index < num_assessments and num_assessments >= 1:  
        #Loop that repeats num_assessments times to fill a list with the names of assessments
        while index < num_assessments:
            
            input_user = input('Type name of assessment\n')
            if (input_user in list_names):
                print('The assessment is already in the list, please put a different name')
                break
            else:    
                list_names.append(input_user)
                input_user = int(input('Please put value of assessment\n'))
                list_values.append(input_user)
                index += 1
            
        print(list_names)
        print(list_values)
        
    elif index != 0 and index == num_assessments:
        break

    else:    
        num_assessments = int(input('Error: you have to put at least 1, please type number of assessments: '))