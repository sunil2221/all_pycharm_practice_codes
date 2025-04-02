with open("2.1 weather_data.csv") as data_file:
    data = data_file.readlines()

    print(data)
# # csv files
# import csv
# with open("2.1 weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     print(data)
#     for row in data:
#         # print(row[1])
#         if row[1] != "temp":
#             temperature.append(row[1])
#     print(temperature)
from typing import Any

# # 3. pandas
# import pandas
from pandas import Series, DataFrame

#
# data = pandas.read_csv("2.1 weather_data.csv")
# print(data)
# print(type(data))
# print(data["temp"])

# # 4.convert data into dict
# data_dict = data.to_dict()
# print(data_dict)

# # convert temp into list
# data_list = data["temp"].to_list()
# print(len(data_list))

# # 5. calculate the max value of temp attribute and mean attribute
# max_value = data["temp"].max()
# print(max_value)
# mean_value = data["temp"].mean()
# print(mean_value)
#
# avg_value = sum(data_list) / len(data_list)
# print(avg_value)
#
# # get data in columns these both acts same
# print(data["condition"])

# data.attribute to print entire column this is an alternate way
# print(data.condition)

# # get data in row
# print(data[data.day == "Tuesday"])
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# farenheit_temp = monday_temp * 9/5 + 32
# print(farenheit_temp)

# 6. create a dataframe from scratch
# data_dict = {
    # "student": ["sunil", "moto", "mano"],
    # "score": [70, 80, 90]

# }

# data_person = pandas.DataFrame(data_dict)
# print(data_person)
# data_person.to_csv("new_data.csv") # name of data.to_csv(new filename)

import pandas
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squrriels_count = len(data[data["Primary Fur Color"] == "Gray"])
# black_squrriels_count = len(data[data["Primary Fur Color"] == "Black"])
# Cinnamon_squrriels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# print(grey_squrriels_count)
# print(black_squrriels_count)
# print(Cinnamon_squrriels_count)
#
#
# data_dict = {
#     "Fur Color": ["Gary", "Cinnamon", "Black"],
#     "Count": [grey_squrriels_count, black_squrriels_count, Cinnamon_squrriels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrrel_count.csv")
