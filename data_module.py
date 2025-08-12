import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_df = pd.read_csv('data/chocolate.csv')

# Remove the column Timestamp from the DataFrame data_df
data_df.drop(columns=['Timestamp'], inplace=True)


def display_dataset_preview():
    pd.set_option('display.max_rows', 1000)
    print(data_df)


def display_visualisation():
    # Make the averages of each column(question 1, 2, 3) in the chocolate data
    averages = data_df.mean()
    colors = ["blue", "orange", "pink"]
    # Make the bars
    bars = plt.bar(averages.index, averages.values, color=colors)

    # Creating a legend for each colour bar
    plt.legend(bars, ["Control", "After unethical practices identification", "After brand recognition"])
    plt.ylabel("Average rating (1-5)")
    plt.title("Average likelihood of consumers buying chocolate (According to awareness)")
    plt.ylim(0, 5)  # Ratings/inclination to buy chocolate goes from 1 to 5(5 being definitely buy)
    plt.show()
    return


def search_data():
    while True:
        print(f"""
                   ____________________________________________________
                  |                 SEARCHING OPTIONS                  |
                  |----------------------------------------------------|
                  | 1. Search all data for a specific question/column  |
                  | 2. Search data for a specific person's responses   |
                   ____________________________________________________""")

        search_options = int(input("""
                  Choose what data you want to search (1 or 2): """))

        if search_options == 1:
            print("""
                   ____________________________________________________
                  |          QUESTION/COLUMN RESPONSE OPTIONS          |
                  |----------------------------------------------------|
                  | 0. Control (inclination to buying chocolate        |     
                  |             in general)                            |   
                  | 1. After unethical practices identification        |
                  |    (Consumers being aware the unknown brand has    |
                  |     several unethical practices)                   |
                  | 2. After brand recognition                         |
                   ____________________________________________________
              """)
            column_options = int(input("""
                  Choose what column/question's data you want to see (0-2): """))
            if column_options == 0 or column_options == 1 or column_options == 2:
                column = data_df.iloc[:,column_options]
                print(column)
            else:
                print("""
                   _____________________________________________________
                  | Invalid selection. Please select a number between 0 |
                  | and 2 (0, 1 or 2).                                  |
                   _____________________________________________________ """) 
                
        elif search_options == 2:
            response_options = int(input("""
                  Choose a response number between 0 and 87: """))
            response = data_df.iloc[response_options,:]
            print(response)
        

        else:
            print("""
                  _____________________________________________________
                 | Invalid selection. Please select the number 1 or 2. |
                  _____________________________________________________""")
            
        print("""
                  ___________________________
                 | Returning to MAIN MENU... |
                  ___________________________""")
        return
