"""
No Linear Relationship (Correlation coefficient = 0)

"""
#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

"""
 we have plotted Max_Pulse against Duration from the full_health_data set.

As you can see, there is no linear relationship between the two variables. It means that longer training session does not lead to higher Max_Pulse.

The correlation coefficient here is 0.

"""
full_health_data = pd.read_csv("data/no_linear_relationship_data.csv", header=0, sep=",")

full_health_data.plot(x ='Duration', y='Max_Pulse', kind='scatter')

plt.show()

#Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

# Save to a file named no_linear_relationship.png
plt.savefig("no_linear_relationship.png")