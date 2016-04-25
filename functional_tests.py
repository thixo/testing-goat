from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith has heard about this great to-do list app
        # She goes to check it out in her browser
        self.browser.get('http://localhost:8000')

        # She's the title mentions the title and page header, so decides she's in the right place
        self.assertIn('TODO:', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to start a to-do list straight away

        # She types "buy some peacock feathers"

        # When she hits enter the page updates and outputs "1 - buy some peacok feathers"

        # There is still a text box for another item

        # She enters "Use peacock feather to make a fly"

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her
        # She sees the site has generated a unique URL for her -- there is some explanatory text to that effect

        # She visits that URL and her to-do list is still there

        # Satisfied she goes back to sleep


if __name__ == '__main__':
    unittest.main()

