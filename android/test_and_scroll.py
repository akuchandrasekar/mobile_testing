import pytest
from time import sleep


@pytest.mark.usefixtures('setup')
class TestScroll():

    def test_scroll(self):
        sleep(3)
        for _ in range(15):
            print(_)
            end_y = 800
            try:
                value = self.driver.find_element_by_id("row_settings").is_displayed()
                if value is True:
                    break
            except:
                self.driver.swipe(470, 1460, 470, end_y, 300)
                self.driver.implicitly_wait(2)
                continue
        sleep(3)
        self.driver.find_element_by_id("row_settings").click()
        sleep(2)
        assert self.driver.find_element_by_xpath('//android.widget.TextView[@text="your_blog_name"]').text == 'your_blog_name'



# start x
# start y
# end x
# end y
# duration