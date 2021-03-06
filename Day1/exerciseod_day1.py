# -*- coding: utf-8 -*-
"""Exerciseod_Day1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hJG_fZmDTViL7a4XigD03ptXPqjFbzM4
"""

!pip install matplotlib

import matplotlib.pyplot as plt

from matplotlib import pyplot as plt

"""# LINE CHART"""

x=[2,5,7,9,10]
y=[20,40,60,80,100]
plt.plot(x, y)
plt.show()

"""# BAR GRAPH"""

x=[2,4,5,7,9]
y=[8,64,125,343,729]
plt.bar(x,y)
plt.title("Demo bar graph")
plt.xlabel("Mark")
plt.ylabel("capacity")
plt.show()

"""# **HISTOGRAM**"""

values=[99.0,100.1,100.2,100.3,100.4,100.5,100.6,100.7]
plt.hist(values)
plt.title("Demo of hist graph")
plt.show()

"""# **Scatter plot**"""

x=[5,2,9,4,7]
y=[125,8,729,64,343]
plt.scatter(x,y)
plt.title("Scatter Plot")
plt.xlabel("number")
plt.ylabel("Queue")
plt.show()

"""# **Scatter plot apply on data set**"""

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("worldometer_snapshots_April18_to_May18.csv")
data.head()

plt.plot(data["Date"],data["Active Cases"])