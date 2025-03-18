import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv("existing_data.csv", header=0, sep=",")

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line')
plt.ylim(ymin=0)
plt.xlim(xmin=0)

"""
When outputting to standard out, the output will be binary data. 
If you are viewing the output in a terminal, it will appear as garbled text.
"""

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()