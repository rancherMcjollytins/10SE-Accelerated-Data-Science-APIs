from datamodule import user_options, check_dependencies, dataDisplayGeneral, dataDisplayPrecise, VisualiseData, UserInfo, SaveSessions
#Just for cool aesthetics.
from otherfunctions import slow_print
#For sys.exit() to close the program
import sys

def main_process():
    slow_print("Welcome to my WeatherAPI Program!", '')
    print()
    print("-----------------------")
    while True:
        userChoice = ""
        for index, value in enumerate(user_options, 1):
            print(f"{index}. {value}")
        print("5. Quit")
        print("-----------------------")
        userChoice = input("Option: ")
        if userChoice.strip() == "1":
            check_dependencies()
        elif userChoice.strip() == "2":
            UserInfo()
        elif userChoice.strip() == "3":
            dataDisplayGeneral()
        elif userChoice.strip() == "4":
            dataDisplayPrecise()
        elif userChoice.strip() == "5":
            print("Closing the program.")
            sys.exit()
        else:
            print("That is not an option!")

main_process()