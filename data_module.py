import pandas as pd

data_df = pd.read_csv('data/chocolate.csv')

# Remove the column Timestamp from the DataFrame data_df
data_df.drop(columns=['Timestamp'], inplace=True)
data_df