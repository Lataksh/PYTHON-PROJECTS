import csv
import numpy
import plotly_express as px

def read_data(path):
    with open(path,newline='') as f:
        raw_data = csv.reader(f)
        days_present = []
        marks = []
        for i in raw_data:
            days_present.append(float(i[1]))
            marks.append(float(i[2]))

        return {"x" : days_present, "y":marks}


def find_correlation(data_source):
    correlation = numpy.corrcoef(data_source["x"], data_source["y"])
    print(correlation[0][1])


def path():
    path = "G:/Whitehat Junior/Python Projects/DataVisualization/marksVsDays.csv"
    data_source = read_data(path)
    find_correlation(data_source)


if __name__ == '__main__':
    path()

