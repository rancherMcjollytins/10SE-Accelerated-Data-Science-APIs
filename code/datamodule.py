"""Google AI explained that ImportError is 
a built-in except that stops the program from
 crashing if packages aren't found."""
try:
    import requests, pandas, matplotlib, json
    print("Packages Found")
except ImportError:
    print("An error occurred with your packages/libraries. See readme for info about requirements.txt")

API_base_url = "http://api.weatherapi.com/v1"
with open('apikeys.txt') as file:
    API_key = file.read()

user_data = {
    'location':"",
    'API Key':""
}

#testing
#'w' in open is for writing format


user_options = ["Verify Dependencies", 
"Manage User Info",
"Fetch API", 
"Display Data", 
"Manage Sessions/Saves",
"Visualise/Graph Data"]

def check_dependencies():
    print("-----------------------")
    userChoice = input("what would you like to do? (Verify Dependencies, Back)")
    if userChoice.lower() == "dependencies":
        try:    
            import requests, pandas, matplotlib, json
            print("all packages imported")
        except ImportError:
            print("You are missing some packages.\nReview README for info on requirements.txt.")
    elif userChoice.lower() == "back":
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
    userChoice = input("What would you like to do?")
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

def dataForecast():

    pass
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
        print(f"current temp in {user_data['location']} is {currentTemp} degrees celsius.\nThe current weather condition in {user_data['location']} is {weatherConditions}")
    else:
        print("An error occurred with your request.")


def SaveSessions():
    filename = 'userData.json'
    try:
        print("Saving Data to Json...")

        '''python cannot json dump to just 'filename', as it is a string.
        We use the as _filename to give the json exactly where to dump the data
        If it was simply dumping to  a string, it wouldn't be able to actually process data dump.
        Gemini/Google AI Mode told me about this bridge-map model, where the string is a map, and
        the file object is the bridge. You need a bridge to drive across. you cant drive across a map.'''
        
        with open(filename, 'w') as _filename:
            json.dump(user_data, _filename)
        """If possible, this is where user activity can be saved by the user, loaded, or deleted."""
    except FileNotFoundError:
        print("An error occurred when saving!")


def VisualiseData():
    pass
    """this is where data will be arranged into charts (matplotlib)"""