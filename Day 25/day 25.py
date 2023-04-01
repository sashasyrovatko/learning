# with open("2.1 weather_data.csv") as data_file:
#     data = data_file.readlines()
# import csv
# with open("2.1 weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#             print(temperatures)

import pandas
# data = pandas.read_csv("2.1 weather_data.csv")
# print((type(data)))
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
# # {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
#  #'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# #[12, 14, 15, 14, 21, 22, 24]
# average = sum(temp_list) / len(temp_list)
# print(data["temp"].mean())
# #17.428571428571427
# larg = data["temp"].nlargest(1)
# print(larg)
# max = data["temp"].max()
# print(max)
# # 24
# print(data[data.day == "Monday"])
# #0  Monday    12     Sunny
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# #0    Sunny
# temp2 = int(monday.temp)
# monday_temp_F = temp2 * 9/5 + 32
# print(monday_temp_F)
# # 53.6
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrel_count)
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

dt = pandas.DataFrame(data_dict)
dt.to_csv("color2.csv")
