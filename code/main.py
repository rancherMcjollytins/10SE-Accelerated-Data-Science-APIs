from datamodule import user_options, user_data, API_key, dataForecast, check_dependencies, locationalFetch, VisualiseData, UserInfo, SaveSessions, displayInfo, UserHelp
#Just for cool aesthetics.
from otherfunctions import slow_print

dataLoad = {}

from datamodule import forecast_info

#For sys.exit() to close the program
import sys
import os
#clears command terminal.
os.system('cls')
def main_process():
    slow_print("Welcome to my WeatherAPI Program!", '')
    print()

    while True:
        userChoice = ""
        print("-----------------------")
        for index, value in enumerate(user_options, 1):
            print(f"{index}. {value}")

        print("-----------------------")
        
        userChoice = input("Option: ")
        if userChoice.strip() == "1":
            check_dependencies()
        elif userChoice.strip() == "2":
            UserInfo()
        elif userChoice.strip() == "3":
            locationalFetch(user_data['location'])
        elif userChoice.strip() == "4":
            displayInfo(locationalFetch(user_data['location']))
        elif userChoice.strip() == "5":
            #load broken
           SaveSessions(user_data)
           #?
        elif userChoice.strip() == "6":
            VisualiseData()
        elif userChoice.strip() == "7":
            UserHelp()
        elif userChoice.strip() == '8':
            dataForecast(None, user_data['location'])
        elif userChoice.strip() == "9":
            print("Closing the program.")
            sys.exit()
        else:
            print("That is not an option!")

main_process()