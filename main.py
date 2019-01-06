import csv
import math

h,w,z = 3,810,0
heart_Arr = [[0 for x in range(w)] for y in range(h)]

with open("heart_rate_history.csv") as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	line_count = 0
	i = 1
	for row in csv_reader:
		if line_count == 0:
			print(f'Column names are {",".join(row)}')
			line_count += 1
		else:
			heart_Arr[0][i] = row[0]
			heart_Arr[1][i] = row[1]
			heart_Arr[2][i] = row[2]
			line_count += 1
			i += 1

total_heart = 0
while z < line_count:
	heart = heart_Arr[2][z]
	heart = str(heart)
	if "-" in heart:
		heart = heart.split("-")
		mean_heart = (int(heart[0]) + int(heart[1]))/2
		total_heart += mean_heart
	else:
		total_heart += int(heart)
	z += 1

mean = total_heart / line_count

y = 1
second_list = []
third_list = []
while y < line_count:
	heart1 = heart_Arr[2][y]
	heart1 = str(heart1)
	if "-" in heart1:
		heart1 = heart1.split("-")
		median_heart = (int(heart1[0]) + int(heart1[1]))/2
		median_heart = abs(median_heart)
		#print(median_heart)
		var1 = math.pow(abs(median_heart) - mean, 2)
		#print(var1)
		second_list.append(var1)
		third_list.append(int(median_heart))
	else:
		#print(abs(int(heart1)))
		var1 = math.pow(abs(int(heart1)) - mean,2)
		#print(var1)
		second_list.append(var1)
		third_list.append(int(heart1))
	y += 1

total_values = sum(second_list)
variance = total_values/len(second_list)
standard_deviation = round(math.sqrt(variance))
perc_deviation = round((standard_deviation/mean)*100)

X = max(third_list)
print(X)
z = (X - round(mean))/standard_deviation

print(total_values," ",variance," ",standard_deviation," ",perc_deviation," ",mean," ",z)
