from selenium import webdriver
import unittest

browser = webdriver.Firefox()

# Edith has heard about this great to-do list app
# She goes to check it out in her browser
browser.get('http://localhost:8000')
try:

    # She's the title mentions the title and page header, so decides she's in the right place
    assert 'TODO:' in browser.title

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

finally:
    browser.quit()