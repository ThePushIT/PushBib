*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Login Page Should Open
    Go To Login Page
    Login Page Should Be Open

Clicking Register Link Should Open Register Page
    Go To Login Page
    Click Link  Create new user
    Register Page Should Be Open