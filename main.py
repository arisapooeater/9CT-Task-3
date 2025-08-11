import time

from data_module import (
    display_dataset_preview,
    display_visualisation,
    search_data,
)

def main_menu():
    while True:
        print(""" _________________________________
                 | \n=== Data Viewer Interface === |
                 |---------------------------------| 
                 | 1. View dataset                 |
                 | 2. View visualisation           |
                 | 3. Search or filter data        |
                 | 4. Exit                         |
                  _________________________________""")


        choese = input(f"Select an option (1-4): ").strip()

        if choese == '1':
            display_dataset_preview()
        elif choese == '2':
            display_visualisation()
        elif choese == '3':
            search_data()
            print("""
                  ________________
                 | Changes saved. |
                  ________________ """)
        elif choese == '4':
            time.sleep(1)
            print("""
                  ____________________
                 | Exiting program..  |
                  ____________________""")
            break
        else:
            print("""
                  ___________________________________________________________
                 |Invalid selection. Please select a number between 1 and 4. |
                  ___________________________________________________________""")


main_menu() 