import csv
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

class Drawer:

    def __init__(self):
        self.x_data = [] 
        self.y_data = []

        self.p_error_data = []
        self.m_error_data = []

        self.colors = ['#9eb3c2', '#51b148', '#c08f7c']
        self.face_colors = ['#a6d683', '#b8f567', '#78bcc0']
        self.edge_colors = ['#2ca388', '#9bcf63', '#dfd4d4']

    def read_csv(self, file_name):

        self.x_data.clear()
        self.y_data.clear()
        self.p_error_data.clear()
        self.m_error_data.clear()

        with open(file_name, newline='') as csvfile:
            data = csv.reader(csvfile, delimiter = ',')

            for row in data:
                self.x_data.append(float(row[0]))
                self.y_data.append(float(row[1]))
                self.p_error_data.append(float(row[2]))
                self.m_error_data.append(float(row[3]))

    def drawing(self, mylabel, smooth):

        fillp = []
        fillm = []

        for i in range(len(self.y_data)):
            fillm.append(self.y_data[i] - self.m_error_data[i]) 
            fillp.append(self.y_data[i] + self.p_error_data[i])

        color_index = random.randint(0,2)

        if(smooth):
            newx = np.linspace(1, len(self.x_data), 300)

            smooth_fillp = spline(self.x_data, fillp, newx)
            smooth_fillm = spline(self.x_data, fillm, newx)
            smooth_y = spline(self.x_data, self.y_data, newx)

            plt.fill_between(newx, smooth_fillp, smooth_fillm, alpha=0.5, edgecolor=self.edge_colors[color_index], facecolor=self.face_colors[color_index], linewidth=1)

            plt.plot(newx,smooth_y,self.colors[color_index], label=mylabel)
        else:
            plt.fill_between(self.x_data, fillp, fillm, alpha=0.5, edgecolor=self.edge_colors[color_index], facecolor=self.face_colors[color_index], linewidth=1)

            plt.plot(self.x_data,self.y_data,self.colors[color_index], label=mylabel)

    def showing(self, title, xlabel, ylabel):

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        plt.show()



draw = Drawer()

draw.read_csv('data2.csv')
draw.drawing('ExampleGraphLabel', True)

draw.read_csv('data.csv')
draw.drawing('ExampleGraphLabel2', True)

draw.showing('ExampleGraph', 'ExamplexLabel', 'Exampleylabel')

    



