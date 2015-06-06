from pandas import *
from ggplot import *
import datetime
import pandasql

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    #turnstile_weather = df
    turnstile_weather['DATEn'] = turnstile_weather.DATEn.apply(lambda x:
            datetime.datetime.strptime(x, "%Y-%m-%d"))
    turnstile_weather['day_of_week'] = turnstile_weather['DATEn'].apply(lambda
            x: x.strftime("%A")).astype("category")
    #turnstile_weather['DATEn'] = to_datetime(turnstile_weather['DATEn'])
        #geom_point() + scale_x_date(labels='%d')  
        #geom_point() + \
    turnstile_weather.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)
    #turnstile_weather.columns.values
    q = """
            select day_of_week, avg(ENTRIESn_hourly) as avg_eph  from turnstile_weather
            group by day_of_week
        """
    df1 = pandasql.sqldf(q.lower(), locals())
    #df1
    #print df1.columns.values
    #df1 = pandasql.sqldf(q, locals())
    plot = ggplot(df1, aes(x = 'factor(day_of_week)', y = 'avg_eph')) + \
        geom_bar(stat = 'bar', color = 'green', fill = 'yellow') + \
        xlab("Day of Week") + ylab("Average entries/hour") + \
        ggtitle('Average number of entries per hour depending on a day of the week')
    return plot

if __name__ == '__main__':
    df = read_csv("turnstile_data_master_with_weather.csv")
    df = df[0:100000]
    print plot_weather_data(df)
