import csv

with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temp = []

    for i in data:
        if i[1] != 'temp':
            temp.append(int(i[1]))
    print(temp)

import pandas


data = pandas.read_csv("weather_data.csv")
print(type(data))

print(data.temp)


print(data["temp"].max())

print(data["condition"])
print(data.condition)

print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
f = (monday.temp*9)/5+32
print(f)


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colours_data = data["Primary Fur Color"].value_counts()

g= (data[data["Primary Fur Color"] == "Gray"])
b= len(data[data["Primary Fur Color"] == "Black"])
c= len(data[data["Primary Fur Color"] == "Cinnamon"])

data = [['Gray',g],['Black',b],['Cinnamon',c]]
dtframe = pandas.DataFrame(data, columns=['color', 'count'])

print(dtframe)
print(type(dtframe))

dtframe.to_csv("squirrel_count")
print(g["Age"])












