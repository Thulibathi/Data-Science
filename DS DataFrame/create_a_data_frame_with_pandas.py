# Import the Pandas library as pd
import pandas as pd

# Define data with column and rows in a variable named d
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

# Create a data frame using the function pd.DataFrame()
# NB: The data frame contains 3 columns and 5 rows
df = pd.DataFrame(data=d)

#Print the data frame output with the print() function
print(df)
