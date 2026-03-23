from datamodule import user_options, check_dependencies, dataDisplayGeneral, dataDisplayPrecise, VisualiseData, UserInfo, SaveSessions
from otherfunctions import slow_print

def main_process():
    check_dependencies()   
    slow_print("Welcome to my WeatherAPI Program!")
    print()
    print("-----------------------")
    while True:
        userChoice = ""
        for index, value in enumerate(user_options, 1):
            print(f"{index}. {value}")
        print("-----------------------")
        userChoice = input("choose")
        if userChoice.strip() == "1":
            check_dependencies()
        break

        

main_process()