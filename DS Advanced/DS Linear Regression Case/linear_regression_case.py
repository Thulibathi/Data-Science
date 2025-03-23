import pandas as pd
import statsmodels.formula.api as smf

"""
* Import the library statsmodels.formula.api as smf. Statsmodels is a statistical library in Python.
* Use the full_health_data set.
* Create a model based on Ordinary Least Squares with smf.ols(). Notice that the explanatory variable must be written first in the parenthesis. Use the full_health_data data set.
* By calling .fit(), you obtain the variable results. This holds a lot of information about the regression model.
* Call summary() to get the table with the results of linear regression.

"""
full_health_data = pd.read_csv("data/full_health_data.csv", header=0, sep=",")

model = smf.ols('Calorie_Burnage ~ Average_Pulse + Duration', data = full_health_data)
results = model.fit()
print(results.summary())
