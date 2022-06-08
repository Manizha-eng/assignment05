# creating an inventory

cd_data = {'ID': ['Student Name', 'Student LastName', 'student DoB']}
# print(cd_data)

cd_data['4545'] = ['Maniza', 'Sadat', '2018']
# print(cd_data)

cd_file = 'cd_inventory.txt'

Student_ID_INDEX = 0
STUDENT_NAME_INDEX = 1
STUDENT_LAST_NAME_INDEX = 2
STUDENT_DoB_INDEX = 3

name = input('Welcome! Please sign your name: ')
print(f'Welcome to {name.title()}\'s college.')
while True:
    # displays menu
    print('Please choose from the following options:')
    print("1. View current inventory", "2. Add new student", "3. Delete student from inventory", "4. Save to file",
          "5. Exit", sep='\n')
    user_input = input('What would you like to do? ')
    import random

    # option 1: display current inventory
    if user_input == '1':
        for key, value in cd_data.items():
            print(f"{key} | {value}")
    # option 2: add new album
    elif user_input == '2':
        student_id = random.randint(1000, 9999)
        student_name = input('Enter your Name: ')
        student_last_name = input('Enter last Name: ')
        student_DoB = input('Enter your DoB (n/a if unknown): ')
        cd_data[student_id] = [student_name.title(), student_last_name.title(), student_DoB]
    # option 3: delete album from inventory
    elif user_input == '3':
        del_student = input('Please enter student ID: ')
        # try:
        for key in cd_data.keys():
            print(key)
            if del_student == key:
                del cd_data[key]
                print(cd_data)
            else:
                print(cd_data)
                break

    elif user_input == '5':
        print('Thank you for accessing your college. Goodbye!')
        break
    else:
        print("That is not a valid input. Please try again.")
