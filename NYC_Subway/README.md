#Project Overview
In this project, we look at the NYC Subway data and figure out if more people ride the subway when it is raining versus when it is not raining.  
We wrangle the NYC subway data, use statistical methods and data visualization to draw an interesting conclusion about the subway dataset that we've analyzed.

#Solutions to problem sets in Udacity *Intro to Data Science* course

##Problem Set 2:
Task #| Task Header | Code/Answer
----|------|------
1 | Number of Rainy Days | num_rainy_days.py
2 | Temp on Foggy and Nonfoggy Days | max_temp_aggregate_by_fog.py  
3 | Mean Temp on Weekends | avg_weekend_temperature.py   
4 | Mean Temp on Rainy Days | avg_min_temperature.py  
5 | Fixing Turnstile Data | fix_turnstile_data.py  
6 | Combining Turnstile Data | create_master_turnstile_file.py  
7 | Filtering Irregular Data | filter_by_regular.py  
8 | Get Hourly Entries | get_hourly_entries.py  
9 | Get Hourly Exits | get_hourly_exits.py  
10 | Time to Hour | time_to_hour.py  
11 | Reformat Subway Dates | reformat_subway_dates.py  

##Problem Set 3:
Task #| Task Header | Code/Answer
----|------|------
1 | Exploratory Data Analysis | entries_histogram.py  
2 | Welch's t-Test? | According to histogram of ENTRIESn_hourly, data are not normally distributed. There are enough observations to guarantee normality of the mean according to CLT. However t-test assumption is that the observations are drawn from the normal distribution. Therefore using t-test may produce wrong results in our case.  
3 | Mann-Whitney U-Test | mann_whitney_plus_means.py  
4 | Ridership on Rainy vs. Nonrainy Days |  The distribution of the number of entries is statistically different between rainy & non-rainy days. See the results description under the table.
5 | Linear Regression | linear_regression_predictions.py  
6 | Plotting Residuals | plot_residuals.py  
7 | Compute R^2 | compute_r_squared.py  
8 | Gradient Descent | sgd_regressor.py   
Description of results:  
We want to see whether the usage of subway in New York increases or decreases depending on rain.  
Independent variable: rainy days  
Dependent variable: Number of subway entries per hour  
Null hypothesis: Average numbers of entries per hour are the same on rainy or non-rainy days.  
Alternative Hypothesis: Average numbers of entries per hour are different on rainy or non-rainy days.  
Type of test: Mann-Whitney U test  
Two tailed p critical: p = 0.0498  
Given significance level of 5% the results are statistically significant and the average usage of subway on rainy days differs from the usage on non-rainy days.  

##Problem Set 4:
Task #| Task Header | Code/Answer
----|------|------
1 | Exercise - Visualization 1 | plot_weather_data.py   
2 | Make Another Visualization | plot_weather_data_2.py   
