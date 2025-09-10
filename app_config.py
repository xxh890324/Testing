from appium.options.android import UiAutomator2Options


# 标准化APP配置测试0901修改
CAPS = {
    "deviceName": " 24090RA29C",
    "automationName": "Appium",
    "platformName": "Android",
    "platformVersion": "14",
    "appPackage": "find.ai.android",
    "appActivity": "find.ai.android.user.ui.login.LoginActivity",
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "dontStopAppOnReset": True,
}

options = UiAutomator2Options()
options.device_name = "24090RA29C"
options.automation_name = "Appium"
options.platform_name = "Android"
options.platform_version = "14"
options.app_package = "find.ai.android"
options.app_activity = "find.ai.android.user.ui.login.LoginActivity"
options.no_reset = True