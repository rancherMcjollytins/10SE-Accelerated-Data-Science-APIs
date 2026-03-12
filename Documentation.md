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
-   User Option and Filtered, Raw and Visualised Data
    - User interacts with the program by inputting a choice (using a CLI string or a GUI input/button) from a list of options to choose which data/data format to display. Program uses different modules for different purposes, to give user the chosen data output.
    -   Program can access the [NASA] API to communicate with, and exchange data from the NASA database, so it can display the data for the user.

### Core Features
-   The core feature of the program is using an API to exchange data between a client and a database, as well as using different tools/libraries to manipulate the data for processing and analysis.

### User Interaction
-   uses a simple GUI (made with tkinter/customtkinter) to act as the primary interface/space between the program and the user for them to react. It will need to provide buttons and intuitive navigation, as well as clear directions for using different modules/functions/processes/commands. (which one is it????)

### Error Fallback
Program uses a try, except statement, as well as loops to fallback in case of unfixable/uncontrollable errors like syntax errors, missing dependencies, etc. This stops full program errors from crashing the system.

---

##  Non-Functional Requirements

### Automatically installs dependencies

### Usability/Accessibility
-   Aesthetically pleasing, intuitive UX (with tools like customtkinter)
    - Aesthetically pleasing GUI with quick navigation for better usability, as well as more accessibility for users of different experience, as opposed to a CLI, which is efficient and useful, but can have a steeper learning curve.
### Efficient transfer of data from database and API to user.

### Management on Errors
-   Errors that will not crash the system, but could compromise the programs' functionality.
    - If the API is down, or an error occurs in fetching, data can not be retrieved. This could be addressed by an operator that will try to access the API, and if unable to, will inform the user that the API is inactive or an error has occurred in fetching the data.
    - Unreliable data can cause misinformation and wrongful analysis, so data must be verified against the database to ensure no loss has occurred throughout the process.