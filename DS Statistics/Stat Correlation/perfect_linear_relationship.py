"""
Perfect Linear Relationship (Correlation Coefficient = 1)
"""
#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

"""
We use scatterplot to visualize the relationship between Average_Pulse and Calorie_Burnage (we have used the-
small data set of the sports watch with 10 observations).

This time we want scatter plots, so we change kind to "scatter":

"""
health_data = pd.read_csv("perfect_linear_relationship_data.csv", header=0, sep=",")

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='scatter'),

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

# Save to a file named linear_relationship.png
plt.savefig("linear_relationship.png")
