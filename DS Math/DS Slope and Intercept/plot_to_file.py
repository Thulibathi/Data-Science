#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv("data/slope_and_intercept_data.csv", header=0, sep=",")

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line'),
plt.ylim(ymin=0, ymax=400)
plt.xlim(xmin=0, xmax=150)

plt.show()

#Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

#Plot to a file named health_plot.png
plt.savefig("health_plot_.png") # 