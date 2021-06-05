import pandas as pd
import plotly.graph_objects as pgo

# reading data and saving as dataframe
path = 'G:/Whitehat Junior/Python Projects/DataVisualization//StudentData.csv'
data = pd.read_csv(path)

# grouping data in level and finding the mean of each data
print(data.groupby("student_id")["attempt"].mean())
# Pandas have a function group by which will group the data according to the conditions given

scatterGraph = pgo.Figure(pgo.Scatter(x=data.groupby("level")["attempt"].mean(),
                                      y=['level1', 'level2', 'level3', 'level4'], orientation='h'))
scatterGraph.show()