grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
student_grades = {}
sorted_students = sorted(students)
for i, sorted_student_grades_list in enumerate(grades):
    sorted_student = list(sorted_students)[i]
    average_grade = sum(sorted_student_grades_list) / len(sorted_student_grades_list)
    student_grades[sorted_student] = average_grade
    print(student_grades)