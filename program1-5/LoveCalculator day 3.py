name1 = input("what is your name: ")
name2 = input('what is your partner name: ')

combined_name = name1 + name2
lower_case = combined_name.lower()

t = lower_case.count('t')
r = lower_case.count('r')
u = lower_case.count('u')
e = lower_case.count('e')
first_digit = t + r + u + e

l = lower_case.count('l')
o = lower_case.count('o')
v = lower_case.count('v')
e = lower_case.count('e')
second_digit = l + o + v + e

love_score1 = str(first_digit) + str(second_digit)
love_score = int(love_score1)
print(love_score)

if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score} you go together like coke and mentos')
elif (love_score > 40) and love_score < 50:
    print(f'your score is {love_score} you are alright together')
else:
    print(f'your score is {love_score}')
