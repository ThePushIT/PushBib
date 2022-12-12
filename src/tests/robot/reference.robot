*** Settings ***
Resource  resource.robot
Suite Setup  Reference Setup
Suite Teardown  Close Test Environment
Test Setup  Go To Login Page And Login User
Test Teardown  Sign Out
Library  SeleniumLibrary

*** Test Cases ***
Add Reference With Authors, Title, Year and Publisher
    Home Page Should Be Open
    Set Reference First Author  Wilma Writer
    Set Reference Title  The best book ever
    Set Reference Year  2000
    Set Reference Publisher  WSOY
    Submit Reference
    Page Should Contain  The best book ever

Add Reference With Missing Author Should Not Work
    Home Page Should Be Open
    Set Reference Title  The best book ever
    Set Reference Year  2000
    Set Reference Publisher  WSOY
    Submit Reference
    Page Should Not Contain  New Author

Add Reference With Missing Name Should Not Work
    Home Page Should Be Open
    Set Reference First Author  New Author
    Set Reference Year  2000
    Set Reference Publisher  WSOY
    Submit Reference
    Page Should Not Contain  New Author

Add Reference With Missing Year Should Not Work
    Home Page Should Be Open
    Set Reference First Author  New Author
    Set Reference Title  The best book ever
    Set Reference Publisher  WSOY
    Submit Reference
    Page Should Not Contain  New Author

Add Reference With Missing Publisher Should Not Work
    Home Page Should Be Open
    Set Reference First Author  New Author
    Set Reference Title  The best book ever
    Set Reference Year  2000
    Submit Reference
    Page Should Not Contain  New Author

Download References Should Work
    Home Page Should Be Open
    Set Reference First Author    New Author
    Set Reference Title    The best book ever
    Set Reference Year    2000
    Set Reference Publisher    WSOY
    Submit Reference
    Download References
    Sleep    2
    Download Directory Should Have A References File

Add Book Reference With Two Authors
    Home Page Should Be Open
    Set Reference First Author  Wilma Writer
    Add New Author
    Set Reference Second Author  Arthur Author
    Set Reference Title  The best book ever
    Set Reference Year  2000
    Set Reference Publisher  WSOY
    Submit Reference
    Page Should Contain  The best book ever
    Page Should Contain  Arthur Author and Wilma Writer

Add Book Reference With Three Authors
    Home Page Should Be Open
    Set Reference First Author  Wilma Writer
    Add New Author
    Set Reference Second Author  Arthur Author
    Add New Author
    Set Reference Third Author  Kaisa Kirjailija
    Set Reference Title  The best book ever
    Set Reference Year  2000
    Set Reference Publisher  WSOY
    Submit Reference
    Page Should Contain  The best book ever
    Page Should Contain  Arthur Author and Kaisa Kirjailija and Wilma Writer

Add Article Reference With Two Authors
    Home Page Should Be Open
    Select From Dropdown  article
    Set Reference First Author  Wilma Writer
    Add New Author
    Set Reference Second Author  Arthur Author
    Add New Author
    Set Reference Third Author  Kaisa Kirjailija
    Set Reference Title  The best book ever
    Set Reference Year  2000
    Set Reference Publisher  WSOY
    Submit Reference
    Page Should Contain  The best book ever
    Page Should Contain  Arthur Author and Kaisa Kirjailija and Wilma Writer

Select Article Type
    Home Page Should Be Open
    Select From Dropdown  article

*** Keywords ***
Set Reference First Author
    [Arguments]  ${author}
    Input Text  author-0  ${author}

Set Reference Second Author
    [Arguments]  ${author}
    Input Text  author-1  ${author}

Set Reference Third Author
    [Arguments]  ${author}
    Input Text  author-2  ${author}

Set Reference Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Reference Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Reference Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

    # to do next
    # testaa miksi dropdown ei toimi osana muuta kutsua
    # korjaa unittestit
    # puske gittiin

Select From Dropdown
    [Arguments]  ${type}
    Wait Until Element is Enabled  type
    Select from list by Label  type   ${type}
    Wait Until Element is Enabled  author-0

Add New Author
    Click Button  Add new author

Submit Reference
    Click Button  Add reference

Download References
    Click Button    download
