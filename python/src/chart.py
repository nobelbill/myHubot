import os
import sys
import math
from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import XYLineChart
from pygooglechart import SparkLineChart
from pygooglechart import Axis

def sparklines(data):
    chart = SparkLineChart(300, 200)
    chart.set_axis_labels(Axis.LEFT, [0, max(data)/2, max(data)])
    chart.set_axis_labels(Axis.BOTTOM, range(0,5))
    
    chart.add_data(data)
    return chart.get_url()