import pytest
from time import sleep


@pytest.mark.usefixtures('setup')
class TestAndLogin():

    def test_and_post(self):
        self.driver.find_element_by_id('fab_button').click()
        sleep(2)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Blog post"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//android.widget.EditText[@index=0]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//android.widget.EditText[@index=0]').send_keys('hello world')
        sleep(2)
        self.driver.find_element_by_id('menu_primary_action').click()
        sleep(2)
        self.driver.find_element_by_xpath('//android.widget.Button[@text="PUBLISH NOW"]').click()
        sleep(5)
        self.driver.find_element_by_id('quick_action_posts_button').click()
        sleep(5)
        assert self.driver.find_element_by_id('title').text == 'hello world'
        assert self.driver.find_element_by_id('date_and_author').text == 'now  ·  your_blog_name'

    def test_and_delete_post(self):
        self.driver.find_element_by_id('quick_action_posts_button').click()
        sleep(3)
        self.driver.find_element_by_id('btn_ternary').click()
        sleep(2)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Bin"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="SCHEDULED"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="BINNED"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Delete permanently"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//android.widget.Button[@text="DELETE"]').click()
        sleep(6)
        assert self.driver.find_element_by_xpath('//android.widget.TextView[@text="You don\'t have any binned posts"]').text.replace('\xa0', ' ') == "You don't have any binned posts"