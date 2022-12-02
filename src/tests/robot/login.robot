*** Settings ***
Resource  resource.robot
Suite Setup  Register Setup
Suite Teardown  Close Browser
Test Setup  Clear Databases

*** Test Cases ***
Login Page Should Open
    Go To Login Page
    Login Page Should Be Open

Clicking Register Link Should Open Register Page
    Go To Login Page
    Click Link  Create new user
    Register Page Should Be Open

Registering New User Should Work
    Go to Register Page
    Set Register Parameters  testuser  testpassword  testpassword
    Register Should Succeed

Registering With Already Taken Username Should Not Work
    Go to Register Page
    Set Register Parameters  testuser  testpassword  testpassword
    Register Should Succeed
    Go to Register Page
    Set Register Parameters  testuser  testpassword  testpassword
    Register Should Fail With Message  Username already reserved

Login With Existing Username Should Work
    Go to Register Page
    Set Register Parameters  testuser  testpassword  testpassword
    Register Should Succeed
    Go To Login Page
    Set Login Parameters  testuser  testpassword
    Login Should Succeed
