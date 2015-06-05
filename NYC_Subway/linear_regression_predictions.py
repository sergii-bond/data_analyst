import numpy as np
import pandas as pd
import statsmodels.api as sm
import datetime

"""
In this question, you need to:
1) implement the linear_regression() procedure
2) Select features (in the predictions procedure) and make predictions.

"""

def linear_regression(features, values):
    """
    Perform linear regression given a data set with an arbitrary number of features.
    
    This can be the same code as in the lesson #3 exercise.
    """
    
    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################
    #features = sm.add_constant(features, prepend = True)
    #ones = pd.Series(np.repeat(1, len(features.index)))
    #ones = pd.DataFrame(ones, index = features.index)
    #features = ones.join(features)
    #features.insert(0, "intercept", ones)
    #features.insert(0, "intercept", 1)
    #values.shape
    #features.shape
    #values.index
    #features.index
    #features
    features = np.insert(features, 0, 1, axis = 1)
    model = sm.OLS(endog = values, exog = features)
    results = model.fit()
    intercept = results.params[0]
    results.params
    params = results.params[1:]
    
    return intercept, params

def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pandas dataframe called weather_turnstile.
    Using the information stored in the dataframe, let's predict the ridership of
    the NYC subway using linear regression with gradient descent.
    
    You can download the complete turnstile weather dataframe here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv    
    
    Your prediction should have a R^2 value of 0.40 or better.
    You need to experiment using various input features contained in the dataframe. 
    We recommend that you don't use the EXITSn_hourly feature as an input to the 
    linear model because we cannot use it as a predictor: we cannot use exits 
    counts as a way to predict entry counts. 
    
    Note: Due to the memory and CPU limitation of our Amazon EC2 instance, we will
    give you a random subet (~10%) of the data contained in 
    turnstile_data_master_with_weather.csv. You are encouraged to experiment with 
    this exercise on your own computer, locally. If you do, you may want to complete Exercise
    8 using gradient descent, or limit your number of features to 10 or so, since ordinary
    least squares can be very slow for a large number of features.
    
    If you receive a "server has encountered an error" message, that means you are 
    hitting the 30-second limit that's placed on running your program. Try using a
    smaller number of features.
    '''
    # Select Features (try different features!)
    dataframe['DATEn'] = dataframe.DATEn.apply(lambda x:
            datetime.datetime.strptime(x, "%Y-%m-%d"))
    dataframe['day_of_week'] = dataframe['DATEn'].apply(lambda
            x: x.weekday())
    dataframe['minute'] = dataframe['TIMEn'].apply(lambda x: int(str.split(x, ':')[1]))
    features = dataframe[['Hour', 'day_of_week', 'minute']]
    
    # Add UNIT to features using dummy variables
    dummy_units = pd.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)
    # Values
    values = dataframe['ENTRIESn_hourly']
    
    # Get the numpy arrays
    features_array = features.values
    values_array = values.values

    # Perform linear regression
    intercept, params = linear_regression(features_array, values_array)
    
    predictions = intercept + np.dot(features_array, params)
    return predictions
