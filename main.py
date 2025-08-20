import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

from data_module import (
    display_dataset_preview,
    display_visualisation,
    search_data,
)

def main_menu():
    time.sleep(1)
    print("""
                🍫 WELCOME TO THE DATA VIEWER INTERFACE 🍫 """)
    time.sleep(1)
    print("""    \x1B[3mRemember to read the README file before interacting with this program!\x1B[23m""") 
    time.sleep(2)

    while True: #Main loop for program so after returning from functions, the same 'main menu' loops again until the user quits.
        print("""
                  ___________________________________________
                 |                 MAIN MENU                 |
                 |-------------------------------------------| 
                 | 1. View dataset                           |
                 | 2. View visualisation (average bar graph) |
                 | 3. Search specific data                   |
                 | 4. EXIT                                   |
                  ___________________________________________""")


        menu_choice = input("""
                 Select an option (1-4): """)
        time.sleep(2)
        os.system('cls') #Clears the screen
        if menu_choice == '1': 
            display_dataset_preview()
        elif menu_choice == '2':
            display_visualisation()
        elif menu_choice == '3':
            search_data()
        elif menu_choice == '4':
            print("""
                  ____________________
                 | Exiting program..  |
                  ____________________""")
            time.sleep(2)
            break #Stops the program
        else:  #Error message 
            print("""
                  ___________________________________________________________
                 |Invalid selection. Please select a number between 1 and 4. |
                  ___________________________________________________________""")
        time.sleep(2)

main_menu() #Run the main program/function