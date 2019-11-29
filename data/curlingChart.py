import csv
import matplotlib.pyplot as plt  

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

		else:
			if (row[0] == '1998') and (row[4] == "CAN"):
				print('1998 medal for canada!')
				m_1998 += 1

			elif (row[0] == '2002') and (row[4] == "CAN"):
				print('2002 medal for canada!')
				m_2002 += 1

			elif (row[0] == '2006') and (row[4] == "CAN"):
				print('2006 medal for canada!')
				m_2006 += 1

			elif (row[0] == '2010') and (row[4] == "CAN"):
				print('2010 medal for canada!')
				m_2010 += 1

			elif (row[0] == '2014') and (row[4] == "CAN"):
				print('2014 medal for canada!')
				m_2014 += 1

# output a chart here! a line chart would probably be best
medalCounts = [m_1998, m_2002, m_2006, m_2010, m_2014]
years = [1998, 2002, 2006, 2010, 2014]

plt.plot(years, medalCounts, color='green', linewidth=4.0)
plt.xlabel('Olympic Year')
plt.ylabel('Medals by Year')
plt.title('Curling Medals for Canada')
plt.show()