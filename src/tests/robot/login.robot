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
    Submit Register
    Register Should Succeed
    Sign Out

Registering With Already Taken Username Should Not Work
    Go to Register Page
    Set Register Parameters  testuser2  testpassword  testpassword
    Submit Register
    Register Should Succeed
    Go to Register Page
    Set Register Parameters  testuser2  testpassword  testpassword
    Submit Register
    Register Should Fail With Message  Username already reserved

Register With Too Short Username Should Not Work
    Go To Register Page
    Set Register Parameters  test  testpassword  testpassword
    Submit Register
    Register Page Should Be Open

Login With Existing Username Should Work
    Go to Register Page
    Set Register Parameters  testuser3  testpassword  testpassword
    Submit Register
    Register Should Succeed
    Sign Out
    Set Login Parameters  testuser3  testpassword
    Submit Login
    Login Should Succeed
    Sign Out

Login With Nonexisting Username Should Not Work
    Go To Login Page
    Set Login Parameters  testuser4  testpassword
    Submit Login
    Login Should Fail With Message  Wrong username or password
