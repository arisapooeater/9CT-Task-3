import pandas as pd
import matplotlib.pyplot as plt

data_df = pd.read_csv('data/chocolate.csv')

# Remove the column Timestamp from the DataFrame data_df
data_df.drop(columns=['Timestamp'], inplace=True)
data_df



def display_dataset_preview():
    pass

def display_visualisation():
    #Create the plot using big_mac_df
    data_df.plot(
        kind= 'grouped bar',
        x= 'Country',
        y= 'AUD_price',
        color= 'pink',
        alpha=0.3,
        title= 'Consumer Inclination to buying chocolate '
                )       

#Show the plot
plt.show()

def search_data():
    pass