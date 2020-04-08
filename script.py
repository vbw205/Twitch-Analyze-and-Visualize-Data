import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Viewers of Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]
viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

plt.bar(range(len(games)), viewers, color = 'mediumslateblue')
plt.title('Viewers of Featured Games')
plt.legend(['Twitch'])
plt.xlabel('Games')
plt.ylabel('Viewers')
ax = plt.subplot()
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.set_xticklabels(games, rotation = 50)

plt.show()
plt.clf()

# Pie Chart: League of Legends Viewers by Country
labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]
countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]
colors = ['yellowgreen', 'lawngreen', 'lightgreen', 'g', 'mediumseagreen', 'mediumaquamarine', 'mediumturquoise', 'darkslategray', 'cadetblue', 'skyblue', 'cornflowerblue', 'darkcyan']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

plt.pie(countries, colors = colors, explode = explode, shadow = True, startangle = 345, autopct = '%1.0f%%', pctdistance = 1.15)
plt.title('League of Legends Viewers by Country')
plt.legend(labels, loc = 'right')

plt.show()
plt.clf()

# Line Graph: Viewers at Each Hour

hour = range(24)
viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]
hour_labels = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
y_upper = [i + (i*0.15) for i in viewers_hour]
y_lower = [i - (i*0.15) for i in viewers_hour]

plt.plot(hour, viewers_hour, color = 'darkblue')
plt.title('Viewers at Each Hour')
plt.xlabel('Hour')
plt.ylabel('Viewers')
plt.legend(['January 1st, 2015'], loc = 4)
ax = plt.subplot()
ax.set_xticks(hour)
ax.set_xticklabels(hour_labels, rotation = 70)
ax.set_yticks([0, 20, 40, 60, 80, 100, 120])
plt.fill_between(hour, y_lower, y_upper, alpha = 0.3)

plt.show()
plt.clf()
