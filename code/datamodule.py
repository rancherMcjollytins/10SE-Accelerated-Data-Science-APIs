"""Google AI explained that ImportError is 
a built-in except that stops the program from
 crashing if packages aren't found."""
try:
    import requests, pandas, matplotlib, json
    print("Packages Found")
except ImportError:
    print("An error occurred with your packages/libraries. See readme for info about requirements.txt")

API_base_url = "http://api.weatherapi.com/v1"
API_key = ""
user_data = {
    'location':"",
    'API Key':""
}


user_options = ["Verify Dependencies", 
"Manage User Info", 
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
    """This will be where users input their locations, keys and other similar info/files.
    This is also where users can manage what data is stored in the program.
    This is where security is more important (i believe) so im gonna need help with this."""

def dataDisplayGeneral():
    pass
    """this will be for general weather data in a large range (user location or specified)"""

def dataDisplayPrecise():
    pass
    """This will be for precise, user location based weather data"""

def SaveSessions():
    pass
    """If possible, this is where user activity can be saved by the user, loaded, or deleted."""

def VisualiseData():
    pass
    """this is where data will be arranged into charts (matplotlib)"""