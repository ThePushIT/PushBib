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

Download Directory Should Have A References File
    File Should Exist    ${DOWNLOAD_DIRECTORY}/references.bib

Go To Home Page
    Go To  ${HOME URL}

Go To Login Page
    Go To  ${LOGIN URL}

Login Page Should Be Open
    Page Should Contain  Log in

Login Page Should Be Open In Finnish
    Page Should Contain  Kirjaudu sisään

Go To Register Page
    Go To  ${REGISTER URL}

Register Page Should Be Open
    Page Should Contain  Sign up

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
    Click Button  Log in

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

Set Book First Author
    [Arguments]  ${author}
    Input Text  author-0-book  ${author}

Set Article First Author
    [Arguments]  ${author}
    Input Text  author-0-article  ${author}
    
    
Set Inproceeding First Author
    [Arguments]  ${author}
    Input Text  author-0-inproceeding  ${author}

Set Misc First Author
    [Arguments]  ${author}
    Input Text  author-0-misc  ${author}

Set Book Title
    [Arguments]  ${title}
    Input Text  title-book  ${title}

Set Article Title
    [Arguments]  ${title}
    Input Text  title-article  ${title}
    
Set Inproceeding Title
    [Arguments]  ${title}
    Input Text  title-inproceeding  ${title}

Set Misc Title
    [Arguments]  ${title}
    Input Text  title-misc  ${title}

Set Book Year
    [Arguments]  ${year}
    Input Text  year-book  ${year}

Set Article Year
    [Arguments]  ${year}
    Input Text  year-article  ${year}

Set Inproceeding Year
    [Arguments]  ${year}
    Input Text  year-inproceeding  ${year}

Set Misc Year
    [Arguments]  ${year}
    Input Text  year-misc  ${year}

Set Book Publisher
    [Arguments]  ${publisher}
    Input Text  publisher-book  ${publisher}

Set Misc Howpublished
    [Arguments]  ${howpublished}
    Input Text  howpublished-misc  ${howpublished}

Set Article Volume
    [Arguments]  ${volume}
    Input Text  volume  ${volume}

Set Article Pages
    [Arguments]  ${pages}
    Input Text  pages  ${pages}

Set Article Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Set Inproceeding Booktitle
    [Arguments]  ${booktitle}
    Input Text  booktitle  ${booktitle}

Set Misc Note
    [Arguments]  ${note}
    Input Text  note-misc  ${note}

Select From Dropdown
    [Arguments]  ${type}
    Wait Until Element is Enabled  type
    Select from List by Value  type   ${type}

Submit Article
    Click Button  id:submit-article

Submit Book
    Click Button  id:submit-book

Submit Inproceeding
    Click Button  id:submit-inproceeding

Submit Misc
    Click Button  id:submit-misc