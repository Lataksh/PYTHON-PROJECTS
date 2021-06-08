import plotly.figure_factory as px
import pandas as pd

data = pd.read_csv("G:\Whitehat Junior\Python Projects\DataVisualization\MobileRating.csv")

scatterGraph = px.create_distplot([data["Avg Rating"]], ["Normal Distribution"])
scatterGraph.show()

