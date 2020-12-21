import plotly.figure_factory as pff
import pandas as pd
import csv
dataList1 = pd.read_csv("data.csv")
height_list= dataList1["Height(Inches)"].tolist()
weight_list= dataList1["Weight(Pounds)"].tolist()
dis_graph1 = pff.create_distplot([height_list],["Height Distribution Data"],show_hist=False)
dis_graph2 = pff.create_distplot([weight_list],["Weight Distribution Data"],show_hist=False)
dis_graph1.show()
dis_graph2.show()