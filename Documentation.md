    #   Documentation <br> 10SE Data Science
---

##  Functional Requirements 
### User Requirements
-   User Interaction to load Data   
    - User can load raw data from a database by fetching and verifying the **NASA** Web API, and can use the program, as well as different libraries and modules.
-   Data Saving
    - Data can be loaded from different files and saved to allow use between sessions.
-   Data Display
    - User can load and view the database in different display forms (e.g. filtered data, raw data, graphs).
### Inputs and Outputs
-   User Option
    - User uses a simple GUI (made with tkinter/customtkinter) to interact with the program and input a choice from a list of options to choose which data/data format to display. Program uses different modules for different purposes, to give user the chosen data output.
### Data Loading
Program can use the [NASA] API to communicate with, and exchange data from the NASA database, so it can display the data for the user.

### Error Fallback
Program uses a try, except statement, as well as loops to fallback in case of unfixable/uncontrollable errors, thus stopping full program errors.

### Core Database
-   The program must be a 
---

##  Non-Functional Requirements
### Automatically installs dependencies
    
### Aesthetically pleasing, intuitive UX (with tools like customtkinter)

### Efficient transfer of data from database and API to user.

### Different formats for displaying data as to be readable and customisable for user preferences
