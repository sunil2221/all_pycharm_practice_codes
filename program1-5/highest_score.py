students = input("how much marks did you get in maths give 5 student marks Note enter the number "
                 "using space separated don't use , and '': \n").split()
print(students)

for student in range(0, len(students)):
    students[student] = int(students[student])
print(students)

highest_score = 0
for n in students:
    if n > highest_score:
        highest_score = n

print(f'the highest score in maths is: {highest_score}')
