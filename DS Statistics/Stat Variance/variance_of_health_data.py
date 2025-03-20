import pandas as pd
import numpy as np

health_data = pd.read_csv("variance_of_health_data.csv", header=0, sep=",")

var = np.var(health_data)

print(var)
