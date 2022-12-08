*** Settings ***
Library  SeleniumLibrary
Library  ./AppLibrary.py
Library    OperatingSystem

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}/references
${LOGIN URL}  http://${SERVER}
${REGISTER URL}  http://${SERVER}/signup
${SIGNOUT_URL}  http://${SERVER}/signout
${DOWNLOAD_DIRECTORY}  /tmp/bib_files


*** Keywords ***
Reference Setup
    Clear Databases
    Open And Configure Browser
    Go To Register Page And Register User
    Register Keyword To Run On Failure  None
    
Register Setup
    Clear Databases
    Open And Configure Browser
    Register Keyword To Run On Failure  None

Open And Configure Browser
    Create Directory    ${DOWNLOAD_DIRECTORY}
    Open Browser  browser=${BROWSER}
    ...  options=add_experimental_option("prefs", {"download.default_directory": "${DOWNLOAD_DIRECTORY}"})
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Close Test Environment
    Remove Directory    ${DOWNLOAD_DIRECTORY}  recursive=True
    Close Browser

Home Page Should Be Open
    Title Should Be  Your references

Download Directory Should Have A File
    Directory Should Not Be Empty    ${DOWNLOAD_DIRECTORY}

Go To Home Page
    Go To  ${HOME URL}

Go To Login Page
    Go To  ${LOGIN URL}

Login Page Should Be Open
    Page Should Contain  Welcome to PushBib!

Go To Register Page
    Go To  ${REGISTER URL}

Register Page Should Be Open
    Page Should Contain  Already have an account? Log in

Go To Register Page And Register User
    Go To Register Page
    Set Register Parameters  kalle  jeejeejee   jeejeejee
    Submit Register
    Home Page Should Be Open
    Sign Out
    
Set Register Parameters
    [Arguments]  ${username}  ${password}  ${password_again}
    Input Text  username  ${username}
    Input Text  password  ${password}
    Input Text   password_again  ${password_again}

Submit Register
    Click Button  Register

Register Should Succeed
    Home Page Should Be Open

Register Should Fail With Message
    [arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Login Parameters
    [Arguments]  ${username}  ${password}
    Input Text  username  ${username}
    Input Text  password  ${password}

Submit Login
    Click Button  Login

Login Should Succeed
    Home Page Should Be Open

Login Should Fail With Message
    [arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Go To Login Page And Login User
    Go To Login Page
    Set Login Parameters  kalle  jeejeejee
    Submit Login
    Home Page Should Be Open

Sign Out
    Go To  ${SIGNOUT_URL}

Logout Setup
    Register Setup
    Go To Register Page
    Set Register Parameters  hemmo  hauhau123  hauhau123
    Submit Register
    
Clear Databases
    Reset Application
    # tyhjennä kaikki testitietokannasta

    
    
