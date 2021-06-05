import csv
from collections import Counter
import statistics

# syntax to open a csv file
with open("G:/Whitehat Junior/Python Projects/DataVisualization/SOCR-HeightWeight.csv", newline='') as f:
    readingData = csv.reader(f)
    data = list(readingData)


data.pop(0)

dataForMean = []
for a in range(len(data)):
    num = data[a][1]
    dataForMean.append(float(num))

# Mean
numberOfObservation = len(dataForMean)
total = 0
for a in dataForMean:
    total = total + a
mean = total / numberOfObservation

print('Mean of the data given is ' + mean.__str__())


# Median

numbersForMedian = len(dataForMean)
sortedData = sorted(dataForMean, key=abs)
evenOrOdd = numbersForMedian % 2

if evenOrOdd == 0:
    median1 = float(dataForMean[numbersForMedian//2])
    median2 = float(dataForMean[numbersForMedian//2 - 1])
    median = (median1 + median2)/2
else:
    median = float(dataForMean[numbersForMedian//2])

print("The length of the data is " + numbersForMedian.__str__())
print("The median of the data is " + median.__str__())


repeatedNumbers = Counter(dataForMean)
DataRange = {
    "60-70": 0,
    "70-80": 0
}

for height, occourance in repeatedNumbers.items():
    if 60 < float(height) < 70:
        DataRange["60-70"] += occourance
    elif 70 < float(height) < 80:
        DataRange["70-80"] += occourance

# print(DataRange)

mode_range, mode_occourance = 0, 0
for range, occourance in DataRange.items():
    if occourance > mode_occourance:
        mode_range, mode_occourance = [int(range.split("-")[0]), int(range.split("-")[1])], occourance
        mode = float((mode_range[0] + mode_range[1]) / 2)

print("The mode of the values is " + mode.__str__())
