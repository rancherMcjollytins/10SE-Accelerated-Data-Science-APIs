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
