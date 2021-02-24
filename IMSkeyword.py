*** Variables ***
${SLE REGISTERED URL}    https://winwin.stgdevops.site/signup
${LOGIN URL}    https://winwin.stgdevops.site
${WINWIN DEPOSIT LIST URL}    https://winwin.stgdevops.site/deposit/list
${IMS LOGIN URL}    https://winwin-bo.stgdevops.site/login
${CMS LOGIN URL}    https://sle-bo.stgdevops.site/login
${IMS LOGIN ACCOUNT}    kenjiadmin
${IMS LOGIN PASSWORD}    aa1234
${USER NAME}    kenji102616
${PASSWORD}     aa1234
${NEW CONFIRM PASSWORD}    aa1234
${CAPTCHA}      8888
${LOGIN FAIL ACCOUNT}    ffff
${LOGIN FAIL PASSWORD}    qwer
${FAIL CONFIRM PASSWORD}    aa2345
${CMS Lottery Vendor}    WINWIN
${CMS LOGIN ACCOUNT}    Rlmg1
${CMS LOGIN PASSWORD}    K(lD44sdD
${DEPOSITVALUE}    10000
${BROWSER}      Chrome

&{IMS}  topmenu=//*[@id="root"]/div/div[2]/header/div[1]/div[1]/h2
...  financemanage=//*[@id="root"]/div/div[3]/div[1]/ul/li[2]/a/div
...  deposithistory=//*[@id="root"]/div/div[3]/div[1]/ul/li[2]/ul/a[2]/li/span[1]
...  manualadjust=//*[@id="root"]/div/div[3]/div[1]/ul/li[2]/ul/a[9]/li
...  reportmanage=//*[@id="root"]/div/div[3]/div[1]/ul/li[5]
...  currentbetreport=//*[@id="root"]/div/div[3]/div[1]/ul/li[5]/ul/a[2]/li
...  transactionreport=//*[@id="root"]/div/div[3]/div[1]/ul/li[5]/ul/a[4]/li
...  playerreport=//*[@id="root"]/div/div[3]/div[1]/ul/li[5]/ul/a[6]/li
...  membermanage=//*[@id="root"]/div/div[3]/div[1]/ul/li[1]
...  playerlist=//*[@id="root"]/div/div[3]/div[1]/ul/li[1]/ul/a[1]/li/span[1]
...  wishname=kenji102616
...  wishname1=人工加钱
...  wishname2=手动加钱
...  wishmoney1=10000.00
...  account=kenji102616

&{MANUAL ADJUST}  manaualadjusttab=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/span[1]
...  manaualadjusthistorytab=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/span[2]
...  addmoneyradio=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/span[3]/label
...  auditcheckbox=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/form/div[2]/div[2]/div/div/div/div[2]/div[4]/div[1]/div/span/label
...  addmoneyyesbtn=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/form/div[3]/div/div[1]/div/div[2]/div[2]/div[3]/div/button[2]
...  acount=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div[4]/div
...  type=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div[6]/div
...  amount=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div[9]/div/div/span

&{TRANSACTION REPORT}  searchbtn=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div[1]/form/div[3]/button[2]
...  acount=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[3]/div
...  type=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[4]/div
...  income=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[5]/div/span
...  mainwallet=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[7]/div

&{PLAYER REPORT}  searchbtn=//*[@id="root"]/div/div[3]/div[2]/div[2]/div/div[2]/form/div[3]/button[2]
...  acount=//*[@id="root"]/div/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/a
...  totalbalance=//*[@id="root"]/div/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[3]/div/span

&{PLAYER LIST}  searchbtn=//*[@id="root"]/div/div[3]/div[2]/div[2]/div/div[2]/form/div[3]/button[2]
...  name=//*[@id="root"]/div/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/a
...  mainmoney=//*[@id="wallet"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div/span
...  totalmoney=//*[@id="wallet"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[4]/div/div/div[2]/span
...  withdrawalcondition=//*[@id="withdrawal"]/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div  
...  bonusamount=//*[@id="withdrawal"]/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[5]/div/span
...  ispass=//*[@id="withdrawal"]/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[10]/div/div
...  transactionlogtab=//*[@id="logs"]/div/div[2]/div/div/div[1]/span[2]
...  transactiontype=//*[@id="logs"]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[3]/div
...  transactionamount=//*[@id="logs"]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[7]/div/span

&{CURRENTBET}  name=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/a
...  issuenumber=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[4]/div
...  game=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[5]/div
...  betchoice=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[7]/div
...  money=//*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[9]/div


*** Keywords ***
開啟瀏覽器並正確進入到IMS後台系統
    Open Browser    ${IMS LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    IMS - 登录
    Sleep    3s

Welcome IMS Page Should Be Open
    Title Should Be    IMS - 登录

輸入IMS登入帳號
    [Arguments]    ${IMS Account}
    Wait Until Element is visible    //*[@id="userid"]
    Input Text    //*[@id="userid"]    ${IMS Account}

輸入IMS登入密碼
    [Arguments]    ${IMS PASSWORD}
    Input Text    //*[@id="password"]    ${IMS PASSWORD}
    Sleep    3s

IMS點擊登入
    Wait Until Element is visible        //*[@id="root"]/div/form/div[3]/div[2]/button
    Click Button    //*[@id="root"]/div/form/div[3]/div[2]/button

檢查登入IMS
    Title Should Be    双赢 IMS - 首頁
    Wait Until Element is visible    (//*[@class="title"])[2]

點擊財務管理
    Wait Until Element Is Visible  ${IMS.financemanage}
    Click Element  ${IMS.financemanage}

點擊存款紀錄
    Wait Until Element is visible    //*[@id="root"]/div/div[3]/div[1]/ul/li[2]/ul/a[2]/li
    sleep    2s
    Click Element    //*[@id="root"]/div/div[3]/div[1]/ul/li[2]/ul/a[2]/li

搜索會員帳號
    Wait Until Element is visible    //*[@id="react-select-4--value-item"]
    Click Element    //*[@id="search"]
    Input Text    //*[@id="search"]    ${USER NAME}

點擊搜索
    Wait Until Element is visible    //*[@id="root"]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/form/div[4]/button[2]
    sleep    2s
    Click Element    //*[@id="root"]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/form/div[4]/button[2]

操作解鎖批准
    sleep    2s
    Wait Until Element is visible    (//i[@class='red icon-lock'])[1]
    sleep    2s
    Click Element    (//i[@class='red icon-lock'])[1]
    sleep    2s
    Wait Until Element is visible    (//i[@class='blue icon-enable'])[1]
    sleep    2s
    Click Element    (//i[@class='blue icon-enable'])[1]
    sleep    2s
    Wait Until Element is visible    (//button[@class='nrc-button'])[2]
    sleep    2s
    Click Element    (//button[@class='nrc-button'])[2]
    Open Page    

填入會員帳號
    Wait Until Element is visible    //*[@id="root"]/div/div[3]/div[2]/div[2]/div/div/form/div[2]/div[1]/label
    sleep    2s
    Click Element    //*[@id="react-select-32--value"]
    Input Text    //*[@id="react-select-32--value"]    ${USER NAME}

選取會員存款銀行
    Wait Until Element is visible    //*[@id="react-select-33--value"]/div[1]
    sleep    2s
    Click Element    //*[@id="react-select-33--value"]/div[1]
    Click Element   (//div[@class="Select-menu-outer"]/div/div)[2]
    
輸入金額10000元
    Wait Until Element Is Visible  id=adjustamt
    Input Text  id=adjustamt  10000
    
填寫備註
    Wait Until Element is visible    //*[@id="remarks"]/div/div/div/div/div/div/div
    sleep    2s
    Input Text    //*[@id="remarks"]/div/div/div/div/div/div/div    ${REMARKS}

點擊提交
    Wait Until Element is visible    //*[@id="root"]/div/div[3]/div[2]/div[2]/div/div/form/div[9]/button[2]
    Click Element    //*[@id="root"]/div/div[3]/div[2]/div[2]/div/div/form/div[9]/button[2]

點擊人工調節金額
    Wait Until Element Is Visible  ${IMS.manualadjust}
    Click Element  ${IMS.manualadjust}  

IMS點擊會員搜索
    Wait Until Element is visible    //*[@id="react-select-3--value"]/div[1]
    sleep    5s
    Input Text    //*[@id="react-select-3--value"]/div[1]    ${USER NAME}

輸入金額
    sleep    2s
    Wait Until Element is visible     //*[@id="depositamt"]
    Input Text    //*[@id="depositamt"]    ${DEPOSITVALUE}
    sleep    2s

點擊加錢鈕
    Wait Until Element Is Enabled  //*[@class="nrc-button button-blue"]
    Click Element  //*[@class="nrc-button button-blue"]

确认新增存款
    Wait Until Element is visible    //*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/form/div[3]/div/div[1]/div/div[2]/div[2]/div[3]/div/button[2]
    Sleep    2s
    Click Button    //*[@id="root"]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/form/div[3]/div/div[1]/div/div[2]/div[2]/div[3]/div/button[2]

確認進行加錢
    Wait Until Element Is Visible  //*[@class="nrc-button submit"]
    Click Element  //*[@class="nrc-button submit"]
    Wait Until Element Is Visible  ${MANUAL ADJUST.addmoneyyesbtn}
    Click Element  ${MANUAL ADJUST.addmoneyyesbtn}
    Wait Until Page Contains  暂无资料

檢查會員帳號_人工調節列表
    Wait Until Page Contains Element  ${MANUAL ADJUST.acount}
    ${nowname}=  Get Text  ${MANUAL ADJUST.acount}
    Run Keyword if  '${nowname}' == '${IMS.wishname}'  Log to Console  'Pass 會員帳號為kenji102616_人工調節列表'
    ...  ELSE  Log to Console  'Fail 會員帳號_人工調節列表' 

檢查調整金額_會員報表
    Wait Until Element Is Visible  //*[@id="serialid"]
    Input Text  //*[@id="serialid"]  ${IMS.membernumber}
    Wait Until Element Is Visible  ${PLAYER REPORT.searchbtn}
    Wait Until Keyword Succeeds  ${5}  ${3}  Click Element  ${PLAYER REPORT.searchbtn}
    Wait Until Page Does Not Contain  暂无资料  ${7}
    Wait Until Element Is Visible  ${PLAYER REPORT.acount}
    Sleep  3s
    ${nowname}=  Get Text  ${PLAYER REPORT.acount}
    Run Keyword if  '${nowname}' == 'kenji102616'  Log to Console  'Pass 會員帳號為kenji102616_會員報表'
    ...  ELSE  Log to Console  'Fail 會員帳號_會員報表'
    Wait Until Element Is Visible  ${PLAYER REPORT.totalbalance}
    ${nowmoney}=  Get Text  ${PLAYER REPORT.totalbalance}
    Run Keyword if  '${nowmoney}' == '10000.00'  Log to Console  'Pass 用戶餘額為 10000.00 _會員報表'
    ...  ELSE  Log to Console  'Fail 用戶餘額_會員報表'

點擊會員管理
    Wait Until Element Is Visible  //*[@id="root"]/div/div[2]/header/div[1]/div[1]/h2
    Click Element  //*[@id="root"]/div/div[2]/header/div[1]/div[1]/h2
    Wait Until Element Is Visible  ${IMS.membermanage}
    Click Element  ${IMS.membermanage}

*** Settings ***
Resource    WW_Common.robot

*** Variables ***
${SLE REGISTERED URL}    https://winwin.stgdevops.site/signup
${LOGIN URL}    https://winwin.stgdevops.site
${IMS LOGIN URL}    https://winwin-bo.stgdevops.site/login
${CMS LOGIN URL}    https://sle-bo.stgdevops.site/login
${IMS LOGIN ACCOUNT}    kenjiadmin
${IMS LOGIN PASSWORD}    aa1234
${USER NAME}    kenji102617
${PASSWORD}     aa1234
${NEW CONFIRM PASSWORD}    aa1234
${CAPTCHA}      8888
${LOGIN FAIL ACCOUNT}    ffff
${LOGIN FAIL PASSWORD}    qwer
${FAIL CONFIRM PASSWORD}    aa2345
${CMS Lottery Vendor}    WINWIN
${CMS LOGIN ACCOUNT}    Rlmg1
${CMS LOGIN PASSWORD}    K(lD44sdD
${BROWSER}      Chrome


*** Keywords ***
開啟瀏覽器並正確進入到IMS後台系統
    Open Browser    ${IMS LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    IMS - 登录
    Sleep    5s

Welcome IMS Page Should Be Open
    Title Should Be    IMS - 登录

正確輸入IMS登入帳號
    [Arguments]    ${IMS LOGIN ACCOUNT}
    Wait Until Element is visible    //*[@id="userid"]
    Input Text    //*[@id="userid"]    ${IMS LOGIN ACCOUNT}

正確輸入IMS登入密碼
    [Arguments]    ${IMS LOGIN PASSWORD}
    Input Text    //*[@id="password"]    ${IMS LOGIN PASSWORD}
    Sleep    3s

IMS點擊登入
    Wait Until Element is visible        //*[@id="root"]/div/form/div[3]/div[2]/button
    Click Button    //*[@id="root"]/div/form/div[3]/div[2]/button

Welcome IMS Lobby Page Should Be Open
    Title Should Be    双赢 IMS - 首頁