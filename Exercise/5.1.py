student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_height = 0
for height in student_heights:
    total_height += height
number_of_student = 0
for number in student_heights:
    number_of_student += 1
    average_height = round(total_height / number_of_student)

print(average_height)
#print(len(student_height))
#print(sum(student_height))