import pytest
from time import sleep


@pytest.mark.usefixtures('setup')
class TestPost():

    def test_post(self):
        self.driver.find_element_by_accessibility_id("floatingCreateButton").click()
        sleep(1)
        self.driver.find_element_by_accessibility_id('blogPostButton').click()
        sleep(3)
        self.driver.find_element_by_xpath('(//XCUIElementTypeOther[@name="Post title. Empty"])[5]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="Add title"]').send_keys('My First Post')
        sleep(2)
        self.driver.find_element_by_xpath('(//XCUIElementTypeOther[@name="Start writing… Horizontal scroll bar, 1 page Vertical scroll bar, 1 page"])[4]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="Start writing…"]').send_keys('Description')
        sleep(2)
        self.driver.find_element_by_accessibility_id('Publish').click()
        sleep(2)
        self.driver.find_element_by_accessibility_id('Publish Now').click()
        sleep(5)
        self.driver.find_element_by_accessibility_id('Posts').click()
        assert self.driver.find_element_by_accessibility_id('My First Post').text == 'My First Post'
        assert self.driver.find_element_by_accessibility_id('Description').text == 'Description'
        assert self.driver.find_element_by_accessibility_id('your_blog_name').text == 'your_blog_name'

    def test_delete_post(self):
        self.driver.find_element_by_accessibility_id('Posts').click()
        sleep(2)
        self.driver.find_element_by_accessibility_id("More").click()
        sleep(1)
        self.driver.find_element_by_accessibility_id("Move to Trash").click()
        sleep(1)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Move to Trash"]').click()
        sleep(3)
        self.driver.find_element_by_accessibility_id('Trashed').click()
        sleep(1)
        self.driver.find_element_by_accessibility_id('More').click()
        sleep(1)
        self.driver.find_element_by_accessibility_id('Delete Permanently').click()
        sleep(1)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Delete Permanently"]').click()
        sleep(3)
        assert self.driver.find_element_by_accessibility_id("You don't have any trashed posts").text == "You don't have any trashed posts"