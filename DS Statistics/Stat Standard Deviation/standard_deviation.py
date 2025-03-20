import pandas as pd
import numpy as np

full_health_data = pd.read_csv("standard_deviation_data.csv", header=0, sep=",")

std = np.std(full_health_data)

print(std)