student_heights = input("Input a list of students heights").split()
for n in range(0, len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)
total_height = 0
for height in student_heights:
    total_height += height
total_num = 0
for num in student_heights:
    total_num += 1
average_height = round(total_height/total_num)
print(average_height)
