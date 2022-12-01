*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Add Reference With Authors, Title, Year and Publisher
    Set Reference Authors  Wilma Writer
    Set Reference Title  The best book ever
    Set Reference Year  2000
    Set Reference Publisher  WSOY
    Submit Reference
    Home Page Should Be Open
    #Page Should Contain  implement robot tests

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

Submit Reference
    Click Button  Add new book