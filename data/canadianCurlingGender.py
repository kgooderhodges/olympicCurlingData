import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Import CSV into Pandas DataFrame
df = pd.read_csv('OlympicsWinter.csv',usecols=["Year", "Sport", "Country", "Gender", "Event", "Medal"])

#Replace spaces in col names with underscore and sets all to lowercase
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

#Filter columns (like country)
df = df[(df.country == "CAN")]
df = df[(df.sport == "Curling")]

#Group dataframe by gender, count medals, unstack and reset index to convert data back into table format
df1 = df.groupby('gender')['medal'].value_counts().unstack().reset_index()

#print df1 to make sure data looks right
#print(df1)

# set width of bar
barWidth = 0.25
 
# set height of bar (used as the Y Axis in plt.bar
bars1 = df1.Gold
bars2 = df1.Silver
bars3 = df1.Bronze
 
# Set position of bar on X axis in plt.bar (this creates the spacing between the bars or they would overlap)
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

 
# Make the plot
plt.bar(r1, bars1, color='Gold', width=barWidth, edgecolor='white', label='Gold')
plt.bar(r2, bars2, color='Silver', width=barWidth, edgecolor='white', label='Silver')
plt.bar(r3, bars3, color='#cd7f32', width=barWidth, edgecolor='white', label='Bronze')
 
# Add xticks on the middle of the group bars and uses df1.gender as the text value
plt.xticks([r + barWidth for r in range(len(bars1))], df1.gender)

#Give it a title
plt.title("Canadian Curling Medals by Gender")

#Give the x and y axes a title
plt.ylabel("Medal Counts")

 
# Adjust the margins
plt.subplots_adjust(bottom= 0.2)


# show me the money
plt.legend()
plt.show()
