import pandas as pd

data_df = pd.read_csv('chocolate.csv')
data_df.head()

# Remove the column ARR_TIME from the DataFrane delays_df

#delays_df = delays_df.drop(['ARR_TIME'],axis=1)
data_df.drop(columns=['ARR_TIME'], inplace=True)
data_df.head()