# Psdeudocodes

### Main
```
Begin Main()
    WHILE true
        FOR EACH index, element IN list_of_user_options
            PRINT {index}. {element}
        ENDFOR
        INPUT choice
        IF choice IS 1 THEN
            CheckDependencies()
        ELIF choice is 2 THEN
            SetUserInfo()
        ELIF choice IS 3 THEN
            FetchAPI()
        ELIF choice IS 4 THEN
            DisplayInfo()
        ELIF choice IS 5 THEN
            SaveData()
        ELiF chpice IS 6 THEN
            VisualiseData()
        ELIF choice IS 7 THEN
            Forecast7Days()
        ELIF choice IS 8 THEN
            EndProgram()
        ELSE
            PRINT That is not an option!
        ENDIF
    ENDWHILE
END MAIN()
```

### User Info (Subroutine 1)
``` 
UserData = {
    UserLocation: "",
    API Key: ""
}

BEGIN SetUserInfo()
    FOREACH item IN UserInfoOptions
        PRINT item
    INPUT UserChoice
    IF UserChoice IS 1 THEN
        DISPLAY UserData[UserLocation]
        INPUT UserLocation
    ELIF UserChoice IS 2 THEN
        Print UserData[API Key]
    ENDIF
End SetUserInfo()
```

### Location Fetch API (Subroutine 2)
```
Begin FetchAPILocational()
    URL = '{API_URL}/current.json?key={APIKEY}&q={CityLocation}'
# Not User Input
    ResponseOutput = INPUT RequestGet(URL)

    IF  API Request Valid THEN
        RETURN ResponseOutput
    ELSE
        DISPLAY 'ERROR'
        RETURN None
    ENDIF
END FetchFetchAPILocational()
```