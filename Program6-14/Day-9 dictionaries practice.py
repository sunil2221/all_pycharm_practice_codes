# dictionary = {
#     "Bug": "an error in a program that prevents the program from running as excepted",
#     "Function": "peace of code that you can easily call over and over again",
#     "Loop": "the action of doing something over and over again"
#
# }
#
# dictionary["Loop"] = "moth ina computer"
# # print(dictionary)
#
# # create empty dictionary
# empty_dictionary = {}
#
# # dictionary = {}
# for key in dictionary:
#     print(key)
#     print(dictionary[key])

# student_score = {
#     "can": 87,
#     "james": 66,
#     "henry": 92,
#     "harry": 96,
#     "leo": 74,
#
# }

# student_grades = {}
# for key in student_score:
#     if student_score[key] > 90:
#         student_grades[key] = "out standing"
#     elif student_score[key] > 80:
#         student_grades[key] = "average"
#     else:
#         student_grades[key] = "good"
#
# print(student_grades)


# capital = {
#     "france": {
#         "cities_visited": ["paris", "lilli", "dijon"], "total_visited": 5
#     },
#     "Germany": {
#         "cities_visited": ["berlin", "HanBurg"], "total_visited": 3
#     }
# }
#
# # nesting dictionary with list
#
travel_log = [
    {
        "country_visited": "France",
        "cities_visited": ["paris", "lilli", "dijon"],
        "times_visited": 5
    },
    {
        "country_visited": "Germany",
        "cities_visited": ["berlin", "HanBurg"],
        "times_visited": 3
    }
]

print(travel_log[0]["country_visited"])

#
# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country_visited"] = country_visited
#     new_country["cities_visited"] = cities_visited
#     new_country["times_visited"] = times_visited
#     travel_log.append(new_country)
#
#
# add_new_country("india", 5, ["Delhi", "mumbai", "andhraPradesh"])
#
# print(travel_log )


num = {
    1: 3,
    2: 6,
    4: 9
}

print(num[4])

