import statistics
import pandas as pd


raw_data = pd.read_csv("./StudentsPerformance.csv")

data = raw_data["math score"].tolist()

populationMean = statistics.mean(data)
populationStandardDeviation = statistics.stdev(data)

print("Population Mean is " + populationMean.__str__())
print("Population Standard Deviation is " + populationStandardDeviation.__str__())

populationStandardDeviation2 = populationStandardDeviation * 2
populationStandardDeviation3 = populationStandardDeviation * 3

meanSumStandardDeviation, meanMinusStandardDeviation = populationMean + populationStandardDeviation, populationMean - populationStandardDeviation
meanSumStandardDeviation2, meanMinusStandardDeviation2= populationMean + populationStandardDeviation2, populationMean - populationStandardDeviation2
meanSumStandardDeviation3, meanMinusStandardDeviation3 = populationMean + populationStandardDeviation3, populationMean - populationStandardDeviation3

listOfFirst = []
for i in data:
    if(i> meanMinusStandardDeviation):
        if(i < meanSumStandardDeviation):
            listOfFirst.append(i)
percent1 = (len(listOfFirst) / len(data)) * 100
print("Percent of 1st standard deviation is " + percent1.__str__() + "%")

listOfSecond = []
for i in data:
    if(i> meanMinusStandardDeviation2):
        if(i < meanSumStandardDeviation2):
            listOfSecond.append(i)
percent2 = (len(listOfSecond) / len(data)) * 100
print("Percent of 2st standard deviation is " + percent2.__str__() + "%")

listOfThird = []
for i in data:
    if(i> meanMinusStandardDeviation3):
        if(i < meanSumStandardDeviation3):
            listOfThird.append(i)
percent3 = (len(listOfThird) / len(data)) * 100
print("Percent of 3st standard deviation is " + percent3.__str__() + "%")