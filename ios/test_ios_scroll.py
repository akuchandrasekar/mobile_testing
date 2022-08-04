import pytest
from time import sleep


@pytest.mark.usefixtures('setup')
class TestScroll():

    def test_scroll(self):
        el = self.driver.find_element_by_accessibility_id('Settings Row')
        self.driver.execute_script('mobile: scroll', {"element": el, "toVisible": True})
        el.click()
        sleep(2)
        assert self.driver.find_element_by_accessibility_id('your_blog_name').text == 'your_blog_name'