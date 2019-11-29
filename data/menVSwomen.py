import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 

m_1998 = 0
m_2002 = 0
m_2006 = 0
m_2010 = 0
m_2014 = 0

categories = []

with open ('curlingData.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

	for row in reader:
		if line_count is 0:
			# parse that first row of text data out of the file
			categories.append (row)
			line_count += 1

# Data
df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21) })
 
# multiple line plot
plt.plot( 'x', 'y1', data=df, marker='', color='skyblue', linewidth=4)
plt.plot( 'x', 'y2', data=df, marker='', color='olive', linewidth=2)
plt.legend()