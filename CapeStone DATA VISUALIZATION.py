import pandas
import plotly_express as px


data = pandas.read_csv('G:/Whitehat Junior/Python Projects/DataVisualization/Copy+of+data+-+data.csv')
graph = px.scatter(data, x = "date", y="cases", labels="country")
graph.show()