#Stargin STEP 4
#Initialization of variables and lists
list_names = []
list_values = []
index = 0
num_assessments = int(input('Please type number of assessments: '))

while(True):
    #Checking if the number of assessments is greater than 1, also, if the lists are not full
    if index < num_assessments and num_assessments >= 1:  
        #Loop that repeats num_assessments times to fill a list with the names of assessments
        while index < num_assessments:
            
            input_user = input('Type name of assessment\n')
            #Checking if the assessment name is in the list
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
    #If the list are full the program ends    
    elif index != 0 and index == num_assessments:
        break
    #If the user input less than 1 assessments the program asks for the number again.
    else:    
        num_assessments = int(input('Error: you have to put at least 1, please type number of assessments: '))