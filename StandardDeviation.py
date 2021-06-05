import pandas
import math

rawData = pandas.read_csv('G:/Whitehat Junior/Python Projects/DataVisualization/StandardDeviation.csv')
data =list(rawData)

sum = 0
for i in data:
    sum = sum + float(i)

mean = sum / len(data)

squaredData = []
for i in data:
    subtractedData = float(i[0]) - mean
    subtractedData = subtractedData ** 2
    squaredData.append(subtractedData)

sumOfSquares = 0
for i in squaredData:
    sumOfSquares += i

subtractedSqrData = sumOfSquares / (len(data) - 1)

StandardDeviation = math.sqrt(subtractedSqrData)

print("The standard deviation of the data given is " + StandardDeviation.__str__())