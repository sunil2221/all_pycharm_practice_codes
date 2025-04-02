# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)


# # new_list = [new_item for item in items]
# numbers = [1, 2, 3]
# # list comprhensions
# new_list = [n+1 for n in numbers]
# print(new_list)
#
# # string as list
# name = "sunil"
# string_list = [letter for letter in name]
# print(string_list)
#
# # range as list
# # new_list = [new_item for item in range]
# range_list = [n*2 for n in range(1,6)]
#
#
# # conditional list comprhension
# # new_condition = [new_item for item in item if test]
# names = ["solo", "duo", "squad", "team"]
# cond_list = [name for name in names if len(name) < 5]
#
#
import random

# 2.
# numbers = [1, 2, 3, 4, 5, 6, 7, 14, 28, 56]
#
# squared_numbers = [n ** 2 for n in numbers]
#
# result = [num for num in numbers if num % 2 == 0]
# print(squared_numbers)
# print(result)

# 3. it gives common element in both list
# file_1_data = [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
# file_2_data = [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]
#
# result = [num for num in file_1_data if num in file_2_data]
# print(result)

# 4. dictionary comprhensions
# names = ["solo", "duo", "squad", "team"]
# import random
#
# student_score = {students: random.randint(1, 100) for students in names}
# print(student_score)
#
# passed_student = {students: score for (students, score) in student_score.items() if score >= 60}
# print(passed_student)
#
# print(student_score)
#
# sentence = "what is the airspeed velocity of an unladen swallow?"
# word_score = {word: random.randint(1, 100) for word in sentence.split()} #.spilt is used to convert list to word
# print(word_score)

# 5.
# whether = {
#
#     "monday": 24,
#     "tuesday": 48,
#     "wednesday": 56,
#     "thursday": 85,
#     "friday": 98
# }
#
# # syntax = {new_key:new_value for (key,value)}
# temp_c_into_temp_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in whether.items()}
#
# print(temp_c_into_temp_f)
#
# student_dict = {
#     "student": ["Angela", "jack", "lily"],
#     "score": [56, 58, 95]
# }
# # # 6.
# # # looping through dictionaries
# # for (key, value) in student_dict.items():
# #     print(value)
#
# import pandas
#
# student_data_frame = pandas.DataFrame
# (student_dict)
# print(student_data_frame)
