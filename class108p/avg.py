import pandas as px 
import  csv
import plotly.figure_factory as ff
df=px.read_csv("dt.csv")
figure=ff.create_distplot([df["Avg Rating"].tolist()],["Avg"],show_hist=False)
figure.show()