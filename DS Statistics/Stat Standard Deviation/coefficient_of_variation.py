"""
The coefficient of variation is used to get an idea of how large the standard deviation is.

Mathematically, the coefficient of variation is defined as:

Coefficient of Variation = Standard Deviation / Mean
"""
import pandas as pd
import numpy as np

full_health_data = pd.read_csv("coefficient_of_variation_data.csv", header=0, sep=",")

cv = np.std(full_health_data) / np.mean(full_health_data)

print(cv)