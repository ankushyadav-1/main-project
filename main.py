import pandas as pd

df = pd.read_csv("C:\\Users\\nname\\Downloads\\IP project work\\main project\\csvOFstudent.csv")

def output():
    print('-' * 145)

def select_any_one_option():
    print('''
        Please select any one option from the menu to proceed.
        ''')

def display_menu():

    print('''
        Welcome to the Student Management System
        Please choose an option from the menu below:
        ''')
    
    output()

    print('''
        1. All Details of All Students
        2. Some Basic Details of All Students
        3. Student Name
        4. Student Roll Number
        5. Student Class & Section
        6. Student Marks
        7. Student Attendance
        8. Student Result
        9. Student Fee
        10. Student Number of Leave
        11. Student Contact
        12. Student Behavior
        13. Student have number of awards
        14. Student make number of Projects
        15. Student take part number of Events
        16. Student enrolled in number of Online Courses
        17. Student have number of Certifications
        18. Student Soft Skills
        19. Student have Communication Skills
        20. Student have Teamwork Skills
        21. Student have Problem Solving Skills
        22. Student have Decision Making Skills
        23. Exit''')
    
    output()
    output()

def All_Details_of_All_Students():
    print(df)
    output()
    output()

def Some_Basic_Details_of_All_Students():
    print(df[['Student Name', 'Student Roll Number', 'Student Class & Section']])
    output()
    output()

def display_student_names():
    while True:
        select_any_one_option()
        print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
        output()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Name', 'Student Class & Section', 'Student Roll Number']])
            output()
        elif choice == 2:
            name = input("Enter the student name: ")
            if name in df['Student Name'].values:
                print(df[df['Student Name'] == name])
                output()
            else:
                print(f"{name} not found in the database.")
                output()
                output()
        elif choice == 3:
            print("Exiting the search for student names.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_roll_numbers():
    select_any_one_option()
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Roll Number', 'Student Name', 'Student Class & Section']])
            output()
        elif choice == 2:
            roll_number = int(input("Enter the student roll number: "))
            if roll_number in df['Student Roll Number'].values:
                print(df[df['Student Roll Number'] == roll_number])
                output()
            else:
                print(f"Student with roll number {roll_number} not found in database.")
                output()
                output()
        elif choice == 3:
            print("Exiting the search for student roll numbers.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_class_section():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Class & Section', 'Student Name', 'Student Roll Number']])
            output()
        elif choice == 2:
            class_section = input("Enter the student class and section: ")
            if class_section in df['Student Class & Section'].values:
                print(df[df['Student Class & Section'] == class_section])
                output()
            else:
                print(f"Student with class and section {class_section} not found in database.")
                output()
                output()
        elif choice == 3:
            print("Exiting the search for student class and section.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_marks():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Marks', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            marks = int(input("Enter the student marks: "))
            if marks in df['Student Marks'].values:
                print(df[df['Student Marks'] == marks])
                output()
            else:
                print(f"Student with marks {marks} not found in database.")
                output()
                output()
        elif choice == 3:
            print("Exiting the search for student marks.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_attendance():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Attendance', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            attendance = input("Enter the student attendance (Present/Absent): ")
            if attendance in df['Student Attendance'].values:
                print(df[df['Student Attendance'] == attendance])
                output()
            else:
                print(f"Student with attendance {attendance} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student attendance.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_details():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df)
            output()
        elif choice == 2:
            name = input("Enter the student name: ")
            if name in df['Student Name'].values:
                print(df[df['Student Name'] == name])   
                output()
            else:
                print(f"Student with name {name} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student details.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_result():   
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Result', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            result = input("Enter the student result (Pass/Fail): ")
            if result in df['Student Result'].values:
                print(df[df['Student Result'] == result])
                output()
            else:
                print(f"Student with result {result} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student results.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_fee():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Fee', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            fee = input("Enter the student fee status (Paid/Unpaid): ")
            if fee in df['Student Fee'].values:
                print(df[df['Student Fee'] == fee])
                output()
            else:
                print(f"Student with fee status {fee} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student fee status.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_number_of_leave():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Number of Leave', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            leave = int(input("Enter the student number of leave: "))
            if leave in df['Student Number of Leave'].values:
                print(df[df['Student Number of Leave'] == leave])
                output()
            else:
                print(f"Student with number of leave {leave} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student number of leave.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_contact():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Contact', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            contact = input("Enter the student contact: ")
            if contact in df['Student Contact'].values:
                print(df[df['Student Contact'] == contact])
                output()
            
            else:
                print(f"Student with contact {contact} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student contact.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_behavior():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Behavior', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            behavior = input("Enter the student behavior: ")
            if behavior in df['Student Behavior'].values:
                print(df[df['Student Behavior'] == behavior])
                output()
            else:
                print(f"Student with behavior {behavior} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student behavior.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_number_of_awards():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Number of Awards', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            awards = int(input("Enter the student number of awards: "))
            if awards in df['Student Number of Awards'].values:
                print(df[df['Student Number of Awards'] == awards])
                output()
            else:
                print(f"Student with number of awards {awards} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student number of awards.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")  
            output()

def display_student_number_of_projects():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Number of Projects', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            projects = int(input("Enter the student number of projects: "))
            if projects in df['Student Number of Projects'].values:
                print(df[df['Student Number of Projects'] == projects])
                output()
            else:
                print(f"Student with number of projects {projects} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student number of projects.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_number_of_events():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Number of Events', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            events = int(input("Enter the student number of events: "))
            if events in df['Student Number of Events'].values:
                print(df[df['Student Number of Events'] == events])
                output()
            else:
                print(f"Student with number of events {events} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student number of events.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_problem_solving_skills():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Problem Solving Skills', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            problem_solving = input("Enter the student problem solving skills (Yes/No): ")
            if problem_solving in df['Student Problem Solving Skills'].values:
                print(df[df['Student Problem Solving Skills'] == problem_solving])
                output()
            else:
                print(f"Student with problem solving skills {problem_solving} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student problem solving skills.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_number_of_certifications():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Number of Certifications', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            certifications = int(input("Enter the student number of certifications: "))
            if certifications in df['Student Number of Certifications'].values:
                print(df[df['Student Number of Certifications'] == certifications])
                output()
            else:
                print(f"Student with number of certifications {certifications} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student number of certifications.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_soft_skills():

    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Soft Skills', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            soft_skills = input("Enter the student soft skills (Yes/No): ")
            if soft_skills in df['Student Soft Skills'].values:
                print(df[df['Student Soft Skills'] == soft_skills])
                output()
            else:
                print(f"Student with soft skills {soft_skills} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student soft skills.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_communication_skills():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Communication Skills', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            communication_skills = input("Enter the student communication skills (Yes/No): ")
            if communication_skills in df['Student Communication Skills'].values:
                print(df[df['Student Communication Skills'] == communication_skills])
                output()
            else:
                print(f"Student with communication skills {communication_skills} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student communication skills.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_teamwork_skills():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Teamwork Skills', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            teamwork_skills = input("Enter the student teamwork skills (Yes/No): ")
            if teamwork_skills in df['Student Teamwork Skills'].values:
                print(df[df['Student Teamwork Skills'] == teamwork_skills])
                output()
            else:
                print(f"Student with teamwork skills {teamwork_skills} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student teamwork skills.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()

def display_student_decision_making_skills():
    print('''
            1. Search for all students
            2. Search for a student
            3. Exit
            ''')
    output()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(df[['Student Decision Making Skills', 'Student Name', 'Student Roll Number', 'Student Class & Section']])
            output()
        elif choice == 2:
            decision_making = input("Enter the student decision making skills (Yes/No): ")
            if decision_making in df['Student Decision Making Skills'].values:
                print(df[df['Student Decision Making Skills'] == decision_making])
                output()
            else:
                print(f"Student with decision making skills {decision_making} not found in database.")
                output()
                output()

        elif choice == 3:
            print("Exiting the search for student decision making skills.")
            output()
            output()
            break
        else:
            print("Invalid choice. Please try again.")
            output()


while True:

    display_menu()

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            All_Details_of_All_Students()

        case 2:
            Some_Basic_Details_of_All_Students()

        case 3:
            display_student_names()

        case 4:
            display_student_roll_numbers()

        case 5:
            display_student_class_section()
            
        case 6:
            display_student_marks()

        case 7:
            display_student_attendance()

        case 8:
            display_student_result()

        case 9:
            display_student_fee()

        case 10:
            display_student_number_of_leave()
            
        case 11:
            display_student_contact()

        case 12:
            display_student_behavior()

        case 13:
            display_student_number_of_awards()

        case 14:
            display_student_number_of_projects

        case 15:
            display_student_number_of_events()

        case 16:
            display_student_problem_solving_skills()

        case 17:
            display_student_number_of_certifications()

        case 18:
            display_student_soft_skills()

        case 19:
            display_student_communication_skills()

        case 20:
            display_student_teamwork_skills()

        case 21:
            display_student_decision_making_skills()

        case 22:
            display_student_problem_solving_skills()

        case 23:
            print("Exiting the program. Have A Nice Day!")
            break

        case _:
            print("Invalid choice. Please try again.")
