from appium import webdriver
import pytest


@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                   desired_capabilities=
                                   {
                                       "platformName": "Android",
                                       "platformVersion": "9",
                                       "deviceName": "android",
                                       "automationName": "uiautomator2",
                                       "app": "/Users/username/Desktop/and/wordpress.apk",
                                       "appPackage": "org.wordpress.android",
                                       "appActivity": "org.wordpress.android.ui.WPLaunchActivity",
                                       "noReset": True,
                                   })
    request.cls.driver = driver
    yield
    driver.quit()
