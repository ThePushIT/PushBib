*** Settings ***
Resource  resource.robot
Suite Setup  Reference Setup
Suite Teardown  Close Test Environment
Test Setup  Go To Login Page And Login User
Test Teardown  Sign Out
Library  SeleniumLibrary
Library  AppLibrary

*** Test Cases ***
Add Book With Authors, Title, Year and Publisher
    Home Page Should Be Open
    Set Book First Author  Writer, Wilma
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
    Page Should Not Contain  Teller, Taylor

Add Book With Missing Name Should Not Work
    Home Page Should Be Open
    Set Book First Author  Teller, Taylor
    Set Book Year  2000
    Set Book Publisher  WSOY
    Submit Book
    Page Should Not Contain  Teller, Taylor

Add Book With Missing Year Should Not Work
    Home Page Should Be Open
    Set Book First Author  Teller, Taylor
    Set Book Title  The best book ever
    Set Book Publisher  WSOY
    Submit Book
    Page Should Not Contain  Teller, Taylor

Add Book With Missing Publisher Should Not Work
    Home Page Should Be Open
    Set Book First Author  Teller, Taylor
    Set Book Title  The best book ever
    Set Book Year  2000
    Submit Book
    Page Should Not Contain  Teller, Taylor

Download References Should Work
    Home Page Should Be Open
    Set Book First Author   Teller, Taylor
    Set Book Title    Magic Handbook
    Set Book Year    2000
    Set Book Publisher    WSOY
    Submit Book
    Download References
    Sleep    2
    Download Directory Should Have A References File

Add Book Reference With Two Authors
    Home Page Should Be Open
    Set Book First Author  Writer, Wilma
    Add New Author Book
    Set Book Second Author  Author, Arthur
    Set Book Title  World Class Writings
    Set Book Year  2000
    Set Book Publisher  WSOY
    Submit Book
    Page Should Contain  World Class Writings
    Page Should Contain  Author, Arthur and Writer, Wilma

Add Book Reference With Three Authors
    Home Page Should Be Open
    Set Book First Author  Writer, Wilma
    Add New Author Book
    Set Book Second Author  Author, Arthur
    Add New Author Book
    Set Book Third Author  Kirjailija, Kaisa
    Set Book Title  May The Force Be With You
    Set Book Year  2000
    Set Book Publisher  WSOY
    Submit Book
    Page Should Contain  May The Force Be With You
    Page Should Contain  Author, Arthur and Kirjailija, Kaisa and Writer, Wilma

Add Article Reference With Three Authors
    Home Page Should Be Open
    Select From Dropdown  article
    Wait Until Page Contains Element  id:author-0-article
    Set Article First Author  Writer, Will
    Add New Author Article
    Set Article Second Author  Author, Astrid
    Add New Author Article
    Set Article Third Author  Kirjailija, Kaisa
    Set Article Title  The best article ever
    Set Article Journal  The best journal ever
    Set Article Year  2000
    Set Article Volume  1
    Set Article Pages  44-46
    Submit Article
    Page Should Contain  The best article ever
    Page Should Contain  Author, Astrid and Kirjailija, Kaisa and Writer, Will

Add Article Reference With Two Authors
    Home Page Should Be Open
    Select From Dropdown  article
    Wait Until Page Contains Element  id:author-0-article
    Set Article First Author  Researcher, Raymond
    Add New Author Article
    Set Article Second Author  Scientist, Stephen
    Set Article Title  The best study ever
    Set Article Journal  The best journal ever
    Set Article Year  2000
    Set Article Volume  1
    Set Article Pages  44-46
    Submit Article
    Page Should Contain  The best study ever
    Page Should Contain  Researcher, Raymond and Scientist, Stephen

Add Inproceeding Reference With Two Authors
    Home Page Should Be Open
    Select From Dropdown  inproceeding
    Wait Until Page Contains Element  id:author-0-inproceeding
    Set Inproceeding First Author  Storyteller, Sean
    Add New Author Inproceeding
    Set Inproceeding Second Author  Author, Arthur
    Set Inproceeding Title  The best inproceeding ever
    Set Inproceeding Booktitle  The best book ever
    Set Inproceeding Year  2000
    Submit Inproceeding
    Page Should Contain  The best inproceeding ever
    Page Should Contain  Author, Arthur and Storyteller, Sean

Add Misc Reference With Two Authors
    Home Page Should Be Open
    Select From Dropdown  misc
    Wait Until Page Contains Element  id:author-0-misc
    Set Misc First Author  Writer, W.
    Add New Author Misc
    Set Misc Second Author  Author, A.
    Set Misc Title  The best misc ever
    Set Misc Howpublished  https://url
    Set Misc Year  2000
    Set Misc Note  Noteworthy note
    Submit Misc
    Page Should Contain  The best misc ever
    Page Should Contain  Noteworthy note

Select Article Type
    Home Page Should Be Open
    Select From Dropdown  article
    Element Should Be Visible  id=article_form

Select Inproceeding Type
    Home Page Should Be Open
    Select From Dropdown  inproceeding
    Element Should Be Visible  id=inproceeding_form

Select Misc Type
    Home Page Should Be Open
    Select From Dropdown  misc
    Element Should Be Visible  id=misc_form

References Should Be In Alphabetical Order By Author
    Set Book First Author  Storyteller, Steve
    Set Book Title  Once upon a time
    Set Book Year  2000
    Set Book Publisher  Comma Press
    Submit Book
    Set Book First Author  Williams, Walter
    Set Book Title  Memoir
    Set Book Year  1830
    Set Book Publisher  Elite Press
    Submit Book
    Set Book First Author  Grey, Earl
    Set Book Title  The Art of Afternoon Tea
    Set Book Year  1993
    Set Book Publisher  Elite Press
    Submit Book
    ${page_content}=  Get Text  class=content
    Reference Order Should Be  ${page_content}  Grey, Earl  Storyteller, Steve  Williams, Walter

*** Keywords ***

Set Book Second Author
    [Arguments]  ${author}
    Input Text  author-1-book  ${author}

Set Book Third Author
    [Arguments]  ${author}
    Input Text  author-2-book  ${author}

Set Article Second Author
    [Arguments]  ${author}
    Input Text  author-1-article  ${author}

Set Article Third Author
    [Arguments]  ${author}
    Input Text  author-2-article  ${author}

Set Inproceeding Second Author
    [Arguments]  ${author}
    Input Text  author-1-inproceeding  ${author}

Set Inproceeding Third Author
    [Arguments]  ${author}
    Input Text  author-2-inproceeding  ${author}

Set Misc Second Author
    [Arguments]  ${author}
    Input Text  author-1-misc  ${author}

Set Misc Third Author
    [Arguments]  ${author}
    Input Text  author-2-misc  ${author}

Add New Author Book
    Click Button  id:book-add-author-field

Add New Author Article
    Click Button  id:article-add-author-field

Add New Author Inproceeding
    Click Button  id:inproceeding-add-author-field

Add New Author Misc
    Click Button  id:misc-add-author-field

Download References
    Click Button    download
