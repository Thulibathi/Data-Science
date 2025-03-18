import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv("existing_data.csv", header=0, sep=",")

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line')
plt.ylim(ymin=0)
plt.xlim(xmin=0)

plt.savefig("health_plot.png") # Saves the plot to a file named health_plot.png