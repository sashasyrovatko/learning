student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
in_list = 0
for numbers in student_scores:
  if numbers > in_list:
   in_list = numbers
print(in_list)
#print(max(student_scores)
