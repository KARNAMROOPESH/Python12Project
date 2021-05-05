import random 
import plotly.figure_factory as ff 
import pandas as pd 

data = pd.read_csv('./data.csv')
rating =  data["Avg Rating"]
datagraph = ff.create_distplot([rating],["Avg Ratings"])
datagraph.show()
