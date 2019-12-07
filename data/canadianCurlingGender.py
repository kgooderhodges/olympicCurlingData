import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv('OlympicsWinter.csv',usecols=["Year", "Sport", "Country", "Gender", "Event", "Medal"])

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')


df = df[(df.country == "CAN")]
df = df[(df.sport == "Curling")]


df1 = df.groupby('gender')['medal'].value_counts().unstack().reset_index()


barWidth = 0.25
 

bars1 = df1.Gold
bars2 = df1.Silver
bars3 = df1.Bronze
 

r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

 

plt.bar(r1, bars1, color='Gold', width=barWidth, edgecolor='white', label='Gold')
plt.bar(r2, bars2, color='Silver', width=barWidth, edgecolor='white', label='Silver')
plt.bar(r3, bars3, color='#cd7f32', width=barWidth, edgecolor='white', label='Bronze')
 

plt.xticks([r + barWidth for r in range(len(bars1))], df1.gender)

plt.title("Canadian Curling Medals by Gender")

plt.ylabel("Medal Counts")

plt.subplots_adjust(bottom= 0.2)

plt.legend()
plt.show()
