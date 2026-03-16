#   Documentation <br> 10SE Data Science

##  Functional Requirements 

### User Requirements

**User Interaction to load Data**
- User can load raw data from a database by fetching and verifying the **NASA** Web API and the users API key. User and program use different libraries and modules.

**Data Display**
- User can load and view the stored data/`  database in different display forms (e.g. filtered data, raw data, graphs).

### Inputs and Outputs

**User Option and Filtered, Raw and Visualised Data.**
- User interacts with the program by inputting a choice (using GUI) from a list of options to choose which data/data format to display. Program uses different modules for different purposes, to give user the chosen data output.

- Program can access the [NASA] API to communicate with, and exchange data from the NASA database, so it can display the data for the user.

### Core Features
-   The core feature of the program is using an API to exchange data between a client and a database, as well as using different tools/libraries to manipulate the data for processing and analysis.

### User Interaction

**GUI**
- uses a simple GUI (made with tkinter/customtkinter) to act as the primary interface/space between the program and the user for them to react. It will need to provide simple, intuitive navigation, as well as clear directions for using different processes and functions.

### Error Fallback
-   Program uses a try, except statement, as well as loops to fallback in case of unfixable/uncontrollable errors like syntax errors, missing dependencies, etc. This stops full program errors from crashing the system.

---

##  Non-Functional Requirements

### Usability/Accessibility

**Aesthetically pleasing, intuitive UX (with tools like customtkinter).**
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

**Preconditions:** NASA API is active, user has Internet connection.
1. On Program Boot
    - When user opens the program, the API is immediately fetched. If not possible, the program will output a message and close.
    - Program automatically imports libraries and infdorms the users if they do not have them installed.
    - The program is visualised for user interaction with a GUI.
2. View Raw Data
    - The user clicks a button to open the raw dataset.
3. Filter Data
    - The user chooses from a list of options or inputs (as a string) what they would like to filter, and the program outputs data that fits the users conditions.
4. Data Visualiser
    - User inputs data they want visualised and program uses matplotlib to transform data into a graph/chart format.

**Postconditions:** User can interact with a database using an API and a GUI. User can views data in the format of filtered, raw or visual information/data.