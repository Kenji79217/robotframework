*** Settings ***
Test Teardown  關閉瀏覽器
Resource  ../../../keywords/NU/NU_Common.robot

*** Test Cases ***
[Z14]登入商城IMS
    [Tags]  NU  BVT  RT  STG  Z14
    開啟瀏覽器並連接到商城IMS
    輸入正確帳密
    點擊登入IMS
    檢查登入IMS

[Z15]不輸入資料登入IMS
    [Tags]  NU  RT  STG  Z15
    開啟瀏覽器並連接到商城IMS
    點擊登入IMS
    檢查不輸入提示IMS

[Z16]輸入錯誤帳密登入IMS
    [Tags]  NU  RT  STG  Z16
    開啟瀏覽器並連接到商城IMS
    輸入錯誤帳密
    點擊登入IMS
    檢查錯誤帳密提示IMS

*** Keywords ***
輸入正確帳密
    NUIMS_login.輸入正確帳號
    NUIMS_login.輸入正確密碼

輸入錯誤帳密
    NUIMS_login.輸入錯誤帳號
    NUIMS_login.輸入錯誤密碼

關閉瀏覽器
    NUIMS_login.關閉瀏覽器