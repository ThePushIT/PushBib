*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Login Page Should Open
    Go To Login Page
    Login Page Should Be Open