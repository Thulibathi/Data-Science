#Find the Variance of Full Data Set
import pandas as pd
import numpy as np

full_health_data = pd.read_csv("variance_of_full_health_data.csv", header=0, sep=",")

var = np.var(full_health_data)

print(var)
