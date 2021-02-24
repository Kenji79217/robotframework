NU_IMS_Keyword.py
*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL IMS}  https://nu-bo.stgdevops.site/login
${BROWSER}  Chrome
&{NUIMS}  ac=lilyqa1
...  pw=a12345
...  acerr=aaabbb
...  pwerr=c1234567
...  acerr2=test


*** Keywords ***
開啟瀏覽器並連接到商城IMS
    Open Browser    ${LOGIN URL IMS}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    IMS - 登录

輸入正確帳號
    Wait Until Element Is Visible  //*[@id="userid"]
    Input Text  //*[@id="userid"]  ${NUIMS.ac}

輸入正確密碼
    Wait Until Element Is Visible  //*[@id="password"]
    Input Text  //*[@id="password"]  ${NUIMS.pw}

輸入錯誤帳號
    Wait Until Element Is Visible  //*[@id="userid"]
    Input Text  //*[@id="userid"]  ${NUIMS.acerr}

輸入錯誤密碼
    Wait Until Element Is Visible  //*[@id="password"]
    Input Text  //*[@id="password"]  ${NUIMS.pwerr}

點擊登入IMS
    Click Element  //*[@class="nrc-button"]
            
檢查登入IMS
    Wait Until Element Is Visible  //div[contains(@class, "nrc-user-id")]  ${8}

檢查不輸入提示IMS
    Wait Until Element Is Visible  //small[contains(text(), "请不要空白")]
    
檢查錯誤帳密提示IMS
    Wait Until Element Is Visible  //h5[contains(text(), "账号或密码错误")]
    
關閉瀏覽器
    Close Browser