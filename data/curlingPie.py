import csv
import matplotlib.pyplot as plt  

golds = []
silvers = []
bronzes = []

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
			if row[7] == 'Gold':
				print('Won Gold!')
				golds.append(row[7])

			elif row[7] == 'Silver':
				print('Won Silver!')
				silvers.append(row[7])

			if row[7] == 'Bronze':
				print('Won Bronze... well we tried')
				bronzes.append(row[7])

			line_count +=1

print('gold medals: ', len(golds))
print('silver medals: ', len(silvers))
print('bronze medals: ', len(bronzes))

labels = ('Gold', 'Silver', 'Bronze')
# sizes are how many and how large the slives of the pie chart will be
sizes = [len(golds), len(silvers), len(bronzes)]
colors = ['gold', 'silver', 'darkgoldenrod']
explode = (0.1, 0, 0)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Gold Medals for Canadian Curling")
plt.xlabel('Medals since 1998')
plt.show()