from appium import webdriver
import pytest


@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                   desired_capabilities={
                                       "platformName": "iOS",
                                       "platformVersion": "13.5",
                                       "deviceName": "iPhone 11 Pro MT",
                                       "automationName": "XCUITest",
                                       "app": "/Users/username/Library/Developer/Xcode/DerivedData/WordPress-bgx/Build/Products/Debug-iphonesimulator/WordPress.app",
                                       "noReset": True,
                                       "autoAcceptAlerts": False
                                   })
    request.cls.driver = driver
    yield
    driver.quit()
