*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Add Reference With Name, Author and Year
    Set Reference Name  The best book ever
    Set Reference Author  Wilma Writer
    Set Reference Year  2000
    Submit Reference
    Home Page Should Be Open
    #Page Should Contain  implement robot tests

*** Keywords ***
Set Reference Name
    [Arguments]  ${name}
    Input Text  name  ${name}

Set Reference Author
    [Arguments]  ${authors}
    Input Text  authors  ${authors}

Set Reference Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Submit Reference
    Click Button  Add reference