*** Settings ***
Resource  resource.robot
Suite Setup  Generic Setup
Suite Teardown  Close Browser
Test Setup  Go To Login Page And Login User

*** Test Cases ***
Add Reference With Authors, Title, Year and Publisher
    Home Page Should Be Open
    Set Reference Authors  Wilma Writer
    Set Reference Title  The best book ever
    Set Reference Year  2000
    Set Reference Publisher  WSOY
    Submit Book
    Page Should Contain  The best book ever

*** Keywords ***
Set Reference Authors
    [Arguments]  ${authors}
    Input Text  authors  ${authors}

Set Reference Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Reference Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Reference Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Submit Book
    Click Button  Add new book
