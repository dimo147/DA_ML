import numpy
import numpy as np
import pandas as pd
from bokeh.plotting import figure
from matplotlib import pyplot as plt
from sklearn import decomposition
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import seaborn as sns

data = np.load("mnist.npz")
x_train = data['x_train']
y_train =data['y_train']
x_test = data['x_test']
y_test = data['y_test']

x_train = np.array([np.ravel(x) for x in x_train])
x_test = np.array([np.ravel(x) for x in x_test])

from bokeh.models import HoverTool, ColumnDataSource

hover = HoverTool(
    # we print the class label
    # and the index in the dataframe
    # in the tooltip
    tooltips = [('label','@label'),
                ('index', '$index')]
)

# create figure
fig_scat = figure(tools=[hover, 'box_zoom', 'crosshair', 'undo'])

# bokeh data source from the dataframe
source = ColumnDataSource(x_train)

# color definition
from bokeh.transform import linear_cmap
from bokeh.palettes import d3
from bokeh.models import CategoricalColorMapper
palette = d3['Category10'][10]
cmap = CategoricalColorMapper(
    factors=np.unique(y_train),
    palette=palette
)

# scatter plot in figure
fig_scat.scatter(
    x='x', y='y', alpha=0.5,
    color={'field': 'label', 'transform': cmap},
    source=source
)

# display below
show(fig_scat)