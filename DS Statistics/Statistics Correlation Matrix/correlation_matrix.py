import pandas as pd

full_health_data = pd.read_csv("correlation_matrix_data.csv", header=0, sep=",")

Corr_Matrix = round(full_health_data.corr(),2)

print(Corr_Matrix)
