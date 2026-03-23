import requests, pandas, matplotlib, json

API_base_url = ""
API_key = ""
user_data = {
    'location':"",
}

user_options = ["Verify/Manage API Key and Depepindencies", 
"Manage User Info", 
"Display Data", 
"Manage Sessions/Saves",
"Visualise/Graph Data"]

def check_dependencies():
    userChoice = input("what would you like to check (api key or dependencies)")
    if userChoice.strip() == 'api key':
        print("ok 1")
    elif userChoice.strip() == "dependencies":
        print("ok 2")
    else:
        print("no work!!!!")

def UserInfo():
    pass
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