from datamodule import check_dependencies
from otherfunctions import slow_print

def main_process():
    check_dependencies()   
    slow_print("Welcome to a WeatherAPI Program!")
    while True:
        userChoice = ""

main_process()