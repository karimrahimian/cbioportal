from plotly.offline import plot
import plotly.graph_objects  as go
import plotly.graph_objs as gogo
import  pandas as pd
import numpy as np
import plotly.express as px
from ..models import Sample,Patient
class Graph():
    def __init__(self):
        self.layout = {
            'title': '',

            'xaxis_title': 'X',
            'yaxis_title': 'Y',
            'font_family': "Nunito",
            'font': dict(
                family="Nunito, monospace",
                size=15,
                color="RebeccaPurple"
            ),
            # 'font_color':"blue",
            'title_font_family': "Nunito",
            # 'title_font_color' : "red",
            # 'legend_title_font_color' : "green"
        }
    def pie_plot_patient(self, pie_data_from_django,title,attribute):
        df = pd.DataFrame(list(pie_data_from_django))
        df.columns = ['Age', 'Sex', 'Race']
        df = df.groupby(attribute).size()
        self.layout['title'] = title
        ff = df.to_numpy()
        print("Gene {}".format(title))
        labels = df.index.tolist()
        values = ff
        pie_plot = gogo.Pie(labels=labels, values=values)
        plot_div = plot({'data': pie_plot, 'layout': self.layout}, output_type='div',image_width=100)
        return plot_div
    def bar_plot_patient(self, pie_data_from_django,title,attribute):
        df = pd.DataFrame(list(pie_data_from_django))
        df.columns = ['Age', 'Sex', 'Race']
        df = df.groupby(attribute).size()
        self.layout['title'] = title

        self.layout['xaxis_title'] = "Age"
        self.layout['yaxis_title'] = "Frequency"

        ff = df.to_numpy()
        print("Gene {}".format(title))
        labels = df.index.tolist()
        values = ff
        pie_plot = gogo.Bar(x=labels,y=values)
        plot_div = plot({'data': pie_plot, 'layout': self.layout}, output_type='div')
        return plot_div
