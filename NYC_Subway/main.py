import numpy as np
import pandas as pd
import pandasql
import csv
import scipy.stats
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.style.use('ggplot')


import linear_regression_predictions as lrp
import sgd_regressor as sgd
import compute_r_squared as r2
import plot_residuals as pr

dataframe = pd.read_csv("turnstile_data_master_with_weather.csv")
#dataframe = dataframe[0:100]
y = dataframe['ENTRIESn_hourly']
#g = lrp.predictions(dataframe)
g = sgd.predictions(dataframe)

print r2.compute_r_squared(y, g) 
hist = pr.plot_residuals(dataframe, g)
hist.show()
