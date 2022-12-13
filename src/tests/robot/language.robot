*** Settings ***
Resource  resource.robot
Test Setup  Register Setup

*** Test Cases ***
Changing Languages Should Work
    Go To Login Page
    Click Link    Suomi
    Login Page Should Be Open In Finnish
    Click Link    English
    Login Page Should Be Open