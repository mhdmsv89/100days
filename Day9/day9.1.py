student_score = {
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}
student_grades = {}


for key in student_score:
    if student_score[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_score[key] >= 81 and student_score[key] < 90:
        student_grades[key] = "Exceeds Expectation"
    elif student_score[key] >= 71 and student_score[key] < 80:
        student_grades[key] = "Acceptable"
    elif student_score[key] < 71 :
        student_grades[key] = "Fail"

print(student_grades)