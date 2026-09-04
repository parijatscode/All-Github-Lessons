# Solution of the Summative Assessment-Job-1:
# Question Paper attached in Github Repository.

# Solution:

student_list = []


# Student Add Functionalities:
def add_student():
    student_id = input("Enter Student Id: ")
    student_name = input("Enter Student Name: ")
    age_student = int(input("Enter Student Age: "))
    department_student = input("Enter Student Department Name: ")
    student_mark = float(input('Enter Student Mark: '))
# Grade System Creation:
    if 80 <= student_mark <= 100:
        student_grade = '1st Division'
    elif 60 <= student_mark <= 79:
        student_grade = '2nd Division'
    elif 40 <= student_mark <= 59:
        student_grade = '3rd Division'
    elif 0 <= student_mark < 40:
        student_grade = 'Fail'
    else:
        print("Mark Must be between 0-100")
        return
# Student Data Storing:
    student_data = {
        'student_id': student_id,
        'student_name': student_name,
        'age_student': age_student,
        'department_student': department_student,
        'student_marks': student_mark,
        'student_grade': student_grade
    }

    student_list.append(student_data)
    print("Student Added Successfully")

# View Student Function Creation:
def view_student():
    if not student_list:
        print("No Student's Data Available")
        return

    for student in student_list:
        print(student)

'''
def view_marks():
    student_id = input("Enter Student Id: ")
    for student in student_list:
        if student['student_id'] == student_id:
            print(f"Student Marks: {student['student_marks']}")
            return
    print("Student Not Found")

'''
def grade_marks():
    if not student_list:
        print("No student records available.")
        return

    for student in student_list:
        print(f"{student['student_name']} -> {student['student_grade']}")


# Student Search:
def search_student():
    student_id = input("Enter Student Id: ")
    for student in student_list:
        if student['student_id'] == student_id:
            print(student)
            return
    print("Student Not Found")


# Delete Student:
def delete_student():
    student_id = input("Enter Student Id: ")
    if len(student_list) == 0:
        print("Student Not Available.")
        return

    for student in student_list:
        if student['student_id'] == student_id:
            student_list.remove(student)
            print("Student Deleted Successfully")
            return
    print("Student Not Found")


while True:
    print('Student Management System: ')
    print('''
    1. Add Student
    2. View Student
    3. Search Student
    4. View Grade
    5. Delete student
    6. Exit
    ''')
    option = input("Enter your choice: ")
    if option == '1':
        add_student()
    elif option == '2':
        view_student()
    elif option == '3':
        search_student()
    elif option == '4':
        grade_marks()
    elif option == '5':
        delete_student()
    elif option == '6':
        break
    else:
        print("Invalid option. Please try again.")