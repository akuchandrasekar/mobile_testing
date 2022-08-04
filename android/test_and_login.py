import pytest
from time import sleep


@pytest.mark.usefixtures('setup')
class TestAndLogin():

    def test_and_login(self):
        self.driver.find_element_by_id('login_button').click()
        sleep(2)
        self.driver.find_element_by_id('input').send_keys('your_email')
        sleep(2)
        self.driver.find_element_by_id('primary_button').click()
        sleep(10)
        self.driver.find_element_by_id('login_enter_password').click()
        sleep(4)
        self.driver.find_element_by_id('input').send_keys('your_password')
        sleep(2)
        self.driver.find_element_by_id('primary_button').click()
        sleep(15)
        self.driver.find_element_by_id('primary_button').click()
        sleep(2)
        assert self.driver.find_element_by_id('my_site_title_label').text == 'your_blog_name'
