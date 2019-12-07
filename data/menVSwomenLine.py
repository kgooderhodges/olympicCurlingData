import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 

menG98 = 0
menG02 = 0
menG06 = 0
menG10 = 0
menG14 = 0

womenG98 = 0
womenG02 = 0
womenG06 = 0
womenG10 = 0
womenG14 = 0

categories = []

with open ('OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

	for row in reader:
		if line_count == 0:
			# parse that first row of text data out of the file
			categories.append (row)
			line_count += 1

		else:
			if (row[0] == '1998') and (row[2] == "Curling") and (row[4] == "CAN") and (row[5] == "Men") and (row[7] == "Gold"):
				print('1998 medal for canada!')
				menG98 += 1

			elif (row[0] == '2002') and (row[2] == "Curling") and (row[4] == "CAN") and (row[5] == "Men") and (row[7] == "Gold"):
				print('2002 medal for canada!')
				menG02 += 1

			elif (row[0] == '2006') and (row[2] == "Curling") and (row[4] == "CAN") and (row[5] == "Men") and (row[7] == "Gold"):
				print('2006 medal for canada!')
				menG06 += 1

			elif (row[0] == '2010') and (row[2] == "Curling") and (row[4] == "CAN") and (row[5] == "Men") and (row[7] == "Gold"):
				print('2010 medal for canada!')
				menG10 += 1

			elif (row[0] == '2014') and (row[2] == "Curling") and (row[4] == "CAN") and (row[5] == "Men") and (row[7] == "Gold"):
				print('2014 medal for canada!')
				menG14 += 1
			
			elif (row[0] == '1998') and (row[2] == "Curling") and (row[4] == "CAN") and (row[5] == "Women") and (row[7] == "Gold"):
				print('1998 medal for canada!')
				womenG98 += 1

			elif (row[0] == '2002') and (row[2] == "Curling") and (row[4] == "CAN") and (row[5] == "Women") and (row[7] == "Gold"):
				print('2002 medal for canada!')
				womenG02 += 1

			elif (row[0] == '2006') and (row[2] == "Curling") and (row[4] == "CAN") and (row[5] == "Women") and (row[7] == "Gold"):
				print('2006 medal for canada!')
				womenG06 += 1

			elif (row[0] == '2010') and (row[2] == "Curling") and (row[4] == "CAN") and (row[5] == "Women") and (row[7] == "Gold"):
				print('2010 medal for canada!')
				womenG10 += 1

			elif (row[0] == '2014') and (row[2] == "Curling") and (row[4] == "CAN") and (row[5] == "Women") and (row[7] == "Gold"):
				print('2014 medal for canada Women!')
				womenG14 += 1

# Data
medalCounts = [menG98, menG02, menG06, menG10, menG14]
medalCountsW = [womenG98, womenG02, womenG06, womenG10, womenG14]
years = ['1998', '2002', '2006', '2010', '2014']

plt.plot(years, medalCounts, color='green', linewidth=4.0)
plt.plot(years, medalCountsW, color='blue', linewidth=4.0)
plt.xlabel('Olympic Year')
plt.ylabel('Medals by Year')
plt.title('Men vs Women Gold Medals')
plt.show()
plt.legend()
