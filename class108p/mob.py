import pandas as px 
import csv
import plotly.figure_factory as ff
df=px.read_csv("da.csv")
figure=ff.create_distplot([df["Mobile Brand"].tolist()],["Mobile"],show_hist=False)
figure.show()