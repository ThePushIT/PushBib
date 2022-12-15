*** Settings ***
Resource  resource.robot
Suite Setup  Reference Setup
Suite Teardown  Close Test Environment
Test Setup  Go To Login Page And Login User
Test Teardown  Sign Out
Library  SeleniumLibrary

*** Test Cases ***
Delete Existing Book Reference
    Home Page Should Be Open
    Set Book First Author  Thomas Cormen
    Set Book Title  Introduction to algorithms
    Set Book Year  1990
    Set Book Publisher  MIT Press
    Submit Book
    Page Should Contain  Introduction to algorithms
    Delete Reference
    Page Should Not Contain  Introduction to algorithms
    
Delete Existing Article Reference
    Home Page Should Be Open
    Select From Dropdown  article
    Wait Until Page Contains Element  id:author-0-article
    Set Article First Author  Silver David
    Set Article Title  Mastering the game of go without human knowledge
    Set Article Journal  Nature
    Set Article Year  2017
    Set Article Volume  1
    Set Article Pages  23-30
    Submit Article
    Page Should Contain  Mastering the game of go without human knowledge
    Delete Reference
    Page Should Not Contain  Arthur Author and Kaisa Kirjailija and Wilma Writer

Delete Existing Inproceeding Reference
    Home Page Should Be Open
    Select From Dropdown  inproceeding
    Wait Until Page Contains Element  id:author-0-inproceeding
    Set Inproceeding First Author  Testauthor
    Set Inproceeding Title  The best inproceeding ever
    Set Inproceeding Booktitle  Collection of the best inproceedings
    Set Inproceeding Year  2022
    Submit Inproceeding
    Page Should Contain  Collection of the best inproceedings
    Delete Reference
    Page Should Not Contain  Collection of the best inproceedings

Delete Existing Misc Reference
    Home Page Should Be Open
    Select From Dropdown  miscellaneous
    Wait Until Page Contains Element  id:author-0-misc
    Set Misc First Author  Testauthor Second
    Set Misc Title  The greatest misc available
    Set Misc Howpublished  https://url
    Set Misc Year  1993
    Set Misc Note  Testnote
    Submit Misc
    Page Should Contain  The greatest misc available
    Delete Reference
    Page Should Not Contain  The greatest misc available

*** Keywords ***
Delete Reference
    Click Button  Delete