*** Settings ***
Resource  resource.robot
Suite Setup  Reference Setup
Suite Teardown  Close Test Environment
Test Setup  Go To Login Page And Login User
Test Teardown  Sign Out
Library  SeleniumLibrary

*** Test Cases ***
Add Book With Authors, Title, Year and Publisher
    Home Page Should Be Open
    Set Book First Author  Wilma Writer
    Set Book Title  The best book ever
    Set Book Year  2000
    Set Book Publisher  WSOY
    Submit Book
    Page Should Contain  The best book ever

Add Book With Missing Author Should Not Work
    Home Page Should Be Open
    Set Book Title  The best book ever
    Set Book Year  2000
    Set Book Publisher  WSOY
    Submit Book
    Page Should Not Contain  New Author

Add Book With Missing Name Should Not Work
    Home Page Should Be Open
    Set Book First Author  New Author
    Set Book Year  2000
    Set Book Publisher  WSOY
    Submit Book
    Page Should Not Contain  New Author

Add Book With Missing Year Should Not Work
    Home Page Should Be Open
    Set Book First Author  New Author
    Set Book Title  The best book ever
    Set Book Publisher  WSOY
    Submit Book
    Page Should Not Contain  New Author

Add Book With Missing Publisher Should Not Work
    Home Page Should Be Open
    Set Book First Author  New Author
    Set Book Title  The best book ever
    Set Book Year  2000
    Submit Book
    Page Should Not Contain  New Author

Download References Should Work
    Home Page Should Be Open
    Set Book First Author   New Author
    Set Book Title    The best book ever
    Set Book Year    2000
    Set Book Publisher    WSOY
    Submit Book
    Download References
    Sleep    2
    Download Directory Should Have A References File

Add Book Reference With Two Authors
    Home Page Should Be Open
    Set Book First Author  Wilma Writer
    Add New Author Book
    Set Book Second Author  Arthur Author
    Set Book Title  The best book ever
    Set Book Year  2000
    Set Book Publisher  WSOY
    Submit Book
    Page Should Contain  The best book ever
    Page Should Contain  Arthur Author and Wilma Writer

Add Book Reference With Three Authors
    Home Page Should Be Open
    Set Book First Author  Wilma Writer
    Add New Author Book
    Set Book Second Author  Arthur Author
    Add New Author Book
    Set Book Third Author  Kaisa Kirjailija
    Set Book Title  The best book ever
    Set Book Year  2000
    Set Book Publisher  WSOY
    Submit Book
    Page Should Contain  The best book ever
    Page Should Contain  Arthur Author and Kaisa Kirjailija and Wilma Writer

Add Article Reference With Three Authors
    Home Page Should Be Open
    Select From Dropdown  article
    Wait Until Page Contains Element  id:author-0-article
    #Click Element  id:author-0
    Set Article First Author  Wilma Writer
    Add New Author Article
    Set Article Second Author  Arthur Author
    Add New Author Article
    Set Article Third Author  Kaisa Kirjailija
    Set Article Title  The best book ever
    Set Article Year  2000
    Set Article Volume  1
    Set Article Pages  44-46
    Submit Article
    Page Should Contain  The best book ever
    Page Should Contain  Arthur Author and Kaisa Kirjailija and Wilma Writer

Add Article Reference With Two Authors
    Home Page Should Be Open
    Select From Dropdown  article
    Wait Until Page Contains Element  id:author-0-article
    #Click Element  id:author-0
    Set Article First Author  Wilma Writer
    Add New Author Article
    Set Article Second Author  Arthur Author
    Set Article Title  The best book ever
    Set Article Journal  The best journal ever
    Set Article Year  2000
    Set Article Volume  1
    Set Article Pages  44-46
    Submit Article
    Page Should Contain  The best book ever
    Page Should Contain  Arthur Author and Wilma Writer


Add Inproceeding Reference With Two Authors
    Home Page Should Be Open
    Select From Dropdown  inproceeding
    Wait Until Page Contains Element  id:author-0-inproceeding
    #Click Element  id:author-0
    Set Inproceeding First Author  Wilma Writer
    Add New Author Inproceeding
    Set Inproceeding Second Author  Arthur Author
    Set Inproceeding Title  The best article ever
    Set Inproceeding Booktitle  The best book ever
    Set Inproceeding Year  2000
    Submit Inproceeding
    Page Should Contain  The best book ever
    Page Should Contain  Arthur Author and Wilma Writer


Select Article Type
    Home Page Should Be Open
    Select From Dropdown  article
    Page Should Contain  article

Select Inproceeding Type
    Home Page Should Be Open
    Select From Dropdown  inproceeding
    Page Should Contain  inproceeding


*** Keywords ***
Set Book First Author
    [Arguments]  ${author}
    Input Text  author-0-book  ${author}

Set Book Second Author
    [Arguments]  ${author}
    Input Text  author-1-book  ${author}

Set Book Third Author
    [Arguments]  ${author}
    Input Text  author-2-book  ${author}


Set Article First Author
    [Arguments]  ${author}
    Input Text  author-0-article  ${author}

Set Article Second Author
    [Arguments]  ${author}
    Input Text  author-1-article  ${author}

Set Article Third Author
    [Arguments]  ${author}
    Input Text  author-2-article  ${author}


Set Inproceeding First Author
    [Arguments]  ${author}
    Input Text  author-0-inproceeding  ${author}

Set Inproceeding Second Author
    [Arguments]  ${author}
    Input Text  author-1-inproceeding  ${author}

Set Inproceeding Third Author
    [Arguments]  ${author}
    Input Text  author-2-inproceeding  ${author}


Set Book Title
    [Arguments]  ${title}
    Input Text  title-book  ${title}

Set Article Title
    [Arguments]  ${title}
    Input Text  title-article  ${title}
    
Set Inproceeding Title
    [Arguments]  ${title}
    Input Text  title-inproceeding  ${title}
    

Set Book Year
    [Arguments]  ${year}
    Input Text  year-book  ${year}

Set Article Year
    [Arguments]  ${year}
    Input Text  year-article  ${year}

Set Inproceeding Year
    [Arguments]  ${year}
    Input Text  year-inproceeding  ${year}

Set Book Publisher
    [Arguments]  ${publisher}
    Input Text  publisher-book  ${publisher}


Set Article Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}
    # to do next
    # testaa miksi dropdown ei toimi osana muuta kutsua
    # korjaa unittestit
    # puske gittiin

Set Article Volume
    [Arguments]  ${volume}
    Input Text  volume  ${volume}


Set Article Pages
    [Arguments]  ${pages}
    Input Text  pages  ${pages}

Set Inproceeding Booktitle
    [Arguments]  ${booktitle}
    Input Text  booktitle  ${booktitle}

Select From Dropdown
    [Arguments]  ${type}
    Wait Until Element is Enabled  type
    Select from List by Value  type   ${type}


Add New Author Book
    Click Button  id:book-add-author-field

Add New Author Article
    Click Button  id:article-add-author-field


Add New Author Inproceeding
    Click Button  id:inproceeding-add-author-field

Submit Article
    Click Button  id:submit-article

Submit Book
    Click Button  id:submit-book

Submit Inproceeding
    Click Button  id:submit-inproceeding


Download References
    Click Button    download
