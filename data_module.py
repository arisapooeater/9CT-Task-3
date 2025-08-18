import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import os

# Read the contents of my csv file chocolate.csv into the dataframe data_df
data_df = pd.read_csv('data/chocolate.csv')

# Remove the column Timestamp from the DataFrame data_df
data_df.drop(columns=['Timestamp'], inplace=True)

# Function for printing the chocolate.csv dataset for the user to see
def display_dataset_preview():
    pd.set_option('display.max_columns', 1000) # Setting column limit to 1000 so all my columns in my data are printed 
    pd.set_option('display.max_rows', 1000) # Setting row limit to 1000 so all 88 rows of my data is printed
    print(data_df)
    time.sleep(2)
    print("""
                  ___________________________
                 | Returning to MAIN MENU... |
                  ___________________________""")
    return #Returning to main while loop in main.py


# Function for visualising the dataframe into a bar graph for the user to see and interact with
def display_visualisation():
    # Find the averages of each column(question 1, 2, 3) in the chocolate data
    averages = data_df.mean() 
    colours = ["blue", "orange", "pink"] # Colours for each bar
    bars = plt.bar(averages.index, averages.values, color=colours) # Make the bars

    plt.ylabel("Average rating (1-5)") #Labelling the y axis
    plt.title("Average likelihood of consumers buying chocolate (According to awareness)") # Labelling the graph
    plt.ylim(0, 5)  # Ratings/inclination to buy chocolate goes from 1 to 5(5 being definitely buy)
    plt.show() # Showing the visualisation to the user
    time.sleep(2)   
    print("""
                  ___________________________
                 | Returning to MAIN MENU... |
                  ___________________________""")
    time.sleep(3)
    os.system('cls')
    return #Returning to main while loop in main.py

# Function for printing specific rows and columns from chocolate.csv
def search_data():
    while True:
        print(f"""
                   ____________________________________________________
                  |                 SEARCHING OPTIONS                  |
                  |----------------------------------------------------|
                  | 1. Search all data for a specific question/column  |
                  | 2. Search data for a specific person's responses   |
                  | 3. RETURN TO MAIN MENU                             |
                   ____________________________________________________""")

        search_options = input("""
                  Choose what data you want to search (1-3): """)
        time.sleep(2)
        os.system('cls')
        if search_options == '1':
            while True:
                print("""
                   ____________________________________________________
                  |          QUESTION/COLUMN RESPONSE OPTIONS          |
                  |----------------------------------------------------|
                  | 0. Control(Before conditions)                      |
                  |    (inclination to buying chocolate before any     |
                  |                                    conditions)     | 
                  | 1. After unethical practices identification        |
                  |    (Consumers being aware the unknown brand has    |
                  |     several unethical practices)                   |
                  | 2. After brand recognition                         |
                  | 3. RETURN TO SEARCHING OPTIONS                     |
                   ____________________________________________________ """)
                column_options = input("""
                  Choose what column/question's data you want to see (0-3): """)
                
                os.system('cls')
                if column_options == '0' or column_options == '1' or column_options == '2':
                    pd.set_option('display.max_rows', 1000) # Setting row limit to 1000 so all 88 rows of my data is printed
                    column_int = int(column_options)
                    column = data_df.iloc[:, column_int]
                    print(column)
                elif column_options == '3':
                    time.sleep(2)
                    print("""
                   ___________________________________
                  | Returning to SEARCHING OPTIONS... |
                   ___________________________________""")
                    time.sleep(3)
                    os.system('cls')
                    break #Returning to searching options while loop
                else:
                    print("""
                   _____________________________________________________
                  | Invalid selection. Please select a number between 0 |
                  | and 2 (0/1/2/3).                                    |
                   _____________________________________________________ """) 
                time.sleep(2)
        elif search_options == '2':
            while True:
                print("""
                   ______________________________________________
                  |            SEARCH RESPONSE OPTIONS           |
                  |----------------------------------------------|
                  |  Choose a response number between 0 and 87   |
                  |                    O R                       |
                  | Type 'R' to return to searching options menu |   
                   ______________________________________________""")
                time.sleep(1)
                response_options = input("""
                   Type your action(0-87 / 'R'): """)
                time.sleep(2)
                os.system('cls')

                if response_options.isdigit():
                    response_int = int(response_options)
                    if 0 <= response_int <= 87:
                        response = data_df.iloc[response_int, :]
                        print(response)
                    else:
                        print("""
                  _________________________________________
                 | Invalid selection. Please type a number |
                 | between 0 and 87                        |           
                  _________________________________________""")

                elif response_options == 'R':
                    print("""
                  ___________________________________
                 | Returning to SEARCHING OPTIONS... |
                  ___________________________________""")
                    time.sleep(2)
                    os.system('cls')
                    break #Returning to searching options menu
                else:
                        print("""
                  ______________________________________________
                 | Invalid selection. Please a number between 0 |            
                 | and 87 OR type 'R' to return to searching    |
                 | options.                                     | 
                  ______________________________________________""")  

                time.sleep(2)       
        
        elif search_options == '3':
            time.sleep(2)
            print("""
                  ___________________________
                 | Returning to MAIN MENU... |
                  ___________________________""")
            os.system('cls')
            return #Returning to main while loop in main.py
            
        else:
            print("""
                  ______________________________________________
                 | Invalid selection. Please a number between 0 |            
                 | and 3 (0/1/2/3).                             | 
                  ______________________________________________""")
        time.sleep(2)   
        
