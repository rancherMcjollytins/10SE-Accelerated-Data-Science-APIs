#   Documentation <br> 10SE Data Science

This program should be able to verify API keys, and communicate with the *'WeatherAPI'* to display weather information based on location for users. It should store important data (e.g. API keys, user location) securely and give users accurate, precise and/or visual weather information. It must have control factors for events that could cause issues with the programs functionality (e.g. API is down, no internet).

##  Functional Requirements 

### User Requirements

**User Interaction to load Data**
- User can load raw data from a database by fetching and verifying the **WeatherAPI** and the users API key. User and program use different libraries and modules.

**Data Display**
- User can load and view the stored data/database in different display forms (e.g. general, precise, graphs).

### Inputs and Outputs

**User Option and Filtered, Raw and Visualised Data.**
- User interacts with the program by inputting a choice (using CLI) from a list of options to choose which data/data format to display. Program uses different modules for different purposes, to give user the chosen data output.

- Program can access the [Weather] API to communicate with, and exchange data from the database, so it can display the data for the user.

### Core Features
-   The core feature of the program is using an API to exchange data between a client and a database, as well as using different tools/libraries to manipulate the data for processing and analysis.

### User Interaction

**CLI**
- uses a simple CLI with basic UX design to act as the primary interface/space between the program and the user for them to react. It will need to provide clear directions for inputting commands to use different processes and functions.

### Error Fallback
-   Program uses a try, except statement, as well as loops to fallback in case of unfixable/uncontrollable errors like syntax errors, missing dependencies, etc. This stops full program errors from crashing the system.

---

##  Non-Functional Requirements

### Usability/Accessibility

**GUI (with tools like customtkinter).**
- Aesthetically pleasing GUI with quick navigation for usability and accessibility for users of different experience.

**Easier installation of dependencies.**
- Dependency packages and libraries are easily installed using a *'requirements.txt'* file and the *pip install -r requirements.txt* command in a command terminal. This will help users quickly and automatically install libraries that are essential for functionality.

### Efficiency and Performance

**Efficient transfer of data from database and API to user.**
- API should be fetched quickly and efficiently (hopefully <= 1 second) and functions/processes should be quick, clean and optimised.

**Save/Load**
- Filtered Data and other important pieces processed data can be saved to/loaded from different filetypes to allow for quick analysis and access between sessions. Additionally, they should be compatible to analyse alongside the originald database.

### Errors Management

**Errors that will not crash the system, but could compromise the programs' functionality.**
- If the API is down, or an error occurs in fetching, data can not be retrieved. This could be addressed by an operator that will try to access the API, and if unable to, will inform the user that the API is inactive or an error has occurred in fetching the data.


### Data Reliability
**Data is sourced from a reputable database.**
    - Data and API are run by/owned by a reputable source, like a government site or a well known company, etc.
    - Unreliable data can cause misinformation, so data must be verified to ensure no loss has occurred throughout the process.

**System Reliability**
- Data shouldn't be lost or corrupted at any point. The program/system should not warp data throughout its processes (e.g. lossy compression).

- Data duplicates and outliers can be identified and/or filtered by users or the program in order to produce accurate results.

**Compatibility**
- Data can be loaded from different files/filetypes to allow use between different files in the database.

---

##  Use Cases

### Main
**Actors:** User

**Preconditions:** Weather API is active, user has Internet connection.
1. On Program Boot
    - When user opens the program, the API is immediately fetched. If not possible, the program will output a message and close.
    - Program automatically imports libraries and infdorms the users if they do not have them installed.
    - The program is abstracted and designed as UI for user interaction.
2. View Raw Data
    - The user inputs a string to open the raw dataset.
3. Filter Data
    - The user inputs (as a string) what they would like to filter, and te program outputs data that fits the users conditions.
4. Data Visualiser
    - User inputs data they want visualised and program uses matplotlib to transform data into a graph/chart format.

**Postconditions:** User can interact with a database using an API and a CLI. User can views data in the format of filtered, raw or visual information/data.

How do virtual environments work?

## Development
 
Main
```
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
```
Data Module
```
"""Google AI explained that ImportError is 
a built-in except that stops the program from
 crashing if packages aren't found."""
try:
    import requests, matplotlib.pyplot, json
    print("Packages Found")
except ImportError:
    print("An error occurred with your packages/libraries. See readme for info about requirements.txt")

API_base_url = "http://api.weatherapi.com/v1"
try:
    with open('apikeys.txt') as file:
        API_key = file.read().strip()
except:
    print("Could not retrieve apikeys.txt file. Are you sure you have it on your PC?")

user_data = {
    'location':"",
    'API Key':"[Hidden]"
}

forecast_info = {}

helpOptions = ['How do I set my location?', 'How do I set my API key?', 'How do I fetch the API?', 'How do I display data?', 'Back']

#testing
#'w' in open is for writing format


user_options = ["Verify Dependencies", 
"Manage User Info",
"Fetch API", 
"Display Data", 
"Manage Sessions/Saves",
"Visualise/Graph Data", "Help", 'Forecast 1 Week',"Quit"]

def check_dependencies():
    print("-----------------------")
    userChoice = input("what would you like to do? (1. Verify Dependencies, 2. Back)")
    if userChoice.strip() == "1":
        try:    
            import requests, pandas, matplotlib, json
            print("all packages imported")
        except ImportError:
            print("You are missing some packages.\nReview README for info on requirements.txt.")
    elif userChoice.strip() == "2":
        print("Going Back")
    else:
        print("Input Error, please try again! (dependencies or back).")

def UserInfo():
    #.items is required to get the pairs in the dictionary
    #(Key and Value)
    print("-----------------------")
    for item, data in user_data.items():
        print(f"{item}: {data}")
    print("-----------------------")
    print("1. Set User Location")
    print("2. View API Key")
    print("3. Back")
    print("-----------------------")
    userChoice = input("What would you like to do?: ")
    if userChoice == '1':
        print(f'You currently have your location set as {user_data['location']}')
        user_data["location"] = input("Set your location: ")
        return(user_data["location"])
    elif userChoice == '2':
        print(f'You have set your API Key as {user_data['API Key']}')
    elif userChoice == '3':
        print()
    else:
        print('An error has occurred with your input.')


        
    """This will be where users input their locations, keys and other similar info/files.
    This is also where users can manage what data is stored in the program.
    This is where security is more important (i believe) so im gonna need help with this."""

#currently not working.
def dataForecast(weather_data_forecast, userCity_forecast):
    forecast_filename = "forecast.json"
    completeURL = f"{API_base_url}/forecast.json?key={API_key}&q={userCity_forecast}&days=7"
    response_output_forecast = requests.get(completeURL)

    if response_output_forecast.status_code  == 200:
        #.json is important to convert to dict
        weather_data_forecast = response_output_forecast.json()

        if weather_data_forecast:
            print("-----------------")
            for i in range(1, 7):
                #debugged with help from AI
                futureTemp = weather_data_forecast["forecast"]["forecastday"][i]['day']["avgtemp_c"]
                futureConditions = weather_data_forecast["forecast"]["forecastday"][i]["day"]["condition"]["text"]
                date = weather_data_forecast['forecast']['forecastday'][i]['date']
                print(f"{date}\n{futureConditions}, {futureTemp} Degrees (c)")
                print()
            print("----------------")
            Choice2 = input("Would you like to save this info to a json for graphing? (yes/no): ")
            if Choice2.lower() == 'yes':
                with open(forecast_filename, 'w') as write_to_forecast:
                    json.dump(futureTemp, write_to_forecast)
                    json.dump(futureConditions, write_to_forecast)
                    json.dump(date, write_to_forecast)

            elif Choice2.lower() == 'no':
                pass
            else:
                print("That is not an option.")
        return response_output_forecast.json()
    
    else: 
        print("An error has occurred while fetching data.")
        return None

"""this will be for future weather data"""

#This will be for fetching precise, user location based weather data
def locationalFetch(userCity):
    #full url for fetching current weather, as shown in the docs for the weatherAPI
    completeURL = f"{API_base_url}/current.json?key={API_key}&q={userCity}"
    
    #Sends HTML request to API
    response_output = requests.get(completeURL)


    #Checks status code to verify request has gone through.
    if response_output.status_code == 200:
        return response_output.json()
    else:
        print("An error has occurred.")
        return None

def displayInfo(fetched_data):
    #?
    if fetched_data:
        #documentation on weatherAPI doc page, as well as weatherAPI explorer.
        #Json files/dictionaries with values of current, sub values of 
        # temp, conditions, and some further sub values like text (sunny, rainy, etc.)
        currentTemp = fetched_data["current"]["temp_c"]
        weatherConditions = fetched_data["current"]['condition']['text']
        currentRegion = fetched_data['location']['region']
        currentArea = fetched_data['location']['name']
        print(f"current temp in {user_data['location']} ({currentArea}, {currentRegion}) is {currentTemp} degrees (celsius).\nThe current weather condition in {user_data['location']} is {weatherConditions}")
    else:
        print("An error occurred with your request.")


def SaveSessions(_user_data):
    filename = 'userData.json'
    print("1. Save")
    print("2. Load")
    userChoice = input("What would you like to do? ")
    if userChoice.strip() == '1':
        try:
            print("Saving Data to Json...")

            '''python cannot json dump to just 'filename', as it is a string.
            We use the as _filename to give the json exactly where to dump the data
            If it was simply dumping to  a string, it wouldn't be able to actually process data dump.
            Gemini/Google AI Mode told me about this bridge-map model, where the string is a map, and
            the file object is the bridge. You need a bridge to drive across. you cant drive across a map.'''
            
            #user_data is a dictionary that saveSessions doesn't access. it can be written as a parameter.
            with open(filename, 'w') as _filename:
                json.dump(_user_data, _filename)
            """If possible, this is where user activity can be saved by the user, loaded, or deleted."""
        except FileNotFoundError:
            print("An error occurred when saving!")
    elif userChoice.strip() == '2':
        print("Load is currently broken. Sorry")
        return
        print("Attempting to load data...")
        try:
            #'r' as default for reading
            #loading is not working.
            with open(filename) as _filename:
                return(json.load(_filename))
        except:
            print("An error occurred when loading!")        
    else:
        print("An error has occurred!")


def VisualiseData():
    try:
        forecastFile = 'forecast.json'
        with open(forecastFile, 'r') as f:
            pass
        print("Visualisation is currently a WIP.")
    except:
        print("Visualisation is a WIP. It is unfortunately non-functional.")

def UserHelp():
    print("--------------")
    for index,item in enumerate(helpOptions, 1):
        print(f"{index}. {item}")
    print("-----------------")
    while True:     
        userHelpChoice = input("Choose an option (1-5):")
        if userHelpChoice == '1':
            print('To set your location, you must navigate to the user data tab (2 in the main menu) and then input 1 to access your user data.')
        elif userHelpChoice == '2':
            print("To set your API key, create a text file in the path named 'apikeys.txt' and paste the API key there.")
        elif userHelpChoice == '3':
            print("To fetch the API, input 3 in the main menu. You need to have the API key, an internet connection and the API must be open.")
        elif userHelpChoice == '4':
            print("You need to fetch the API first, then navigate to the 4th option in the main menu to display your data.")
        elif userHelpChoice == '5':
            print("Returning to menu.")
            break
        else:
            print("That is not an option!")

```