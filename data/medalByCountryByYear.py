import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Import CSV into Pandas DataFrame
df = pd.read_csv('OlympicsWinter.csv',usecols=["Year", "Sport", "Country", "Medal"])


#Replace spaces in col names with underscore and sets all to lowercase
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

#Filter columns (like country)
pd.to_datetime('year', format='%Y', errors='ignore')
df = df[(df.sport == "Curling")]
df = df[(df.year > 1980)]
#Group dataframe by gender, count medals, unstack and reset index to convert data back into table format
df1 = df.groupby(['country'])['medal'].value_counts().unstack().reset_index()
df1.loc[:,'Row_Total'] = df1.iloc[:, -4:].sum(axis=1) 
df2 = df1[['country','Row_Total']].copy()
df2 = df2.sort_values('Row_Total', ascending=False)

print(df2)
#plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

values = df2['Row_Total']
#colors = ['b', 'g', 'r', 'c', 'm', 'y', 'purple', 'gold']
labels = df2['Row_Total']
explode = (0.1, 0, 0,0,0,0,0,0)
plt.pie(values, labels= labels, shadow=True)


#Give it a title
plt.title("Curling Medals by Country")

#Give the x and y axes a title
#plt.ylabel("Medal Counts")

 
# Adjust the margins
#plt.subplots_adjust(bottom= 0.2)


# show me the money
plt.legend(df2.country,loc='right', bbox_to_anchor = [1.3, 0.5],shadow=True, ncol=1)
plt.show()
