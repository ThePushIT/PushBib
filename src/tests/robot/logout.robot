*** Settings ***
Resource  resource.robot
Suite Setup  Logout Setup
Suite Teardown  Close Browser

*** Test Cases ***
Clicking Sign Out Link After Registration Redirects To Login Page
    Home Page Should Be Open
    Click Link  Sign out
    Login Page Should Be Open

Clicking Sign Out Link After Signing In Redirects To Login Page
    Set Login Parameters  hemmo  hauhau123
    Submit Login
    Home Page Should Be Open
    Click Link  Sign out
    Login Page Should Be Open
