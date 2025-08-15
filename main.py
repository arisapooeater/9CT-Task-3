import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from data_module import (
    display_dataset_preview,
    display_visualisation,
    search_data,
)

def main_menu():
    while True:
        print("""
                  _________________________________
                 |       Data Viewer Interface     |
                 |---------------------------------| 
                 | 1. View dataset                 |
                 | 2. View visualisation           |
                 | 3. Search specific data         |
                 | 4. Exit                         |
                  _________________________________""")


        menu_choice = int(input("""
                 Select an option (1-4): """))
        time.sleep(2)
        if menu_choice == 1:
            display_dataset_preview()
        elif menu_choice == 2:
            display_visualisation()
        elif menu_choice == 3:
            search_data()
        elif menu_choice == 4:
            print("""
                  ____________________
                 | Exiting program..  |
                  ____________________""")
            time.sleep(2)
            break
        else:
            print("""
                  ___________________________________________________________
                 |Invalid selection. Please select a number between 1 and 4. |
                  ___________________________________________________________""")


main_menu() 