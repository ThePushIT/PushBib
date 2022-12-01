*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  127.0.0.1:5000
${BROWSER}  chrome
${DELAY}  0.5 seconds
${LOGIN URL}  http://${SERVER}
${REGISTER URL}  http://${SERVER}/signup

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Go To Login Page
    Go To  ${LOGIN URL}

Login Page Should Be Open
    Page Should Contain  Welcome to PushPib!

Go To Register Page
    Go To  ${REGISTER URL}

Register Page Should Be Open
    Page Should Contain  Already have an account? Log in
