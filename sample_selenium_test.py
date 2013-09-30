#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver


if __name__ == "__main__":
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", "en-us,en,ja")
    fp.update_preferences()

    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={
            'platform': 'ANY',
            'browserName': 'firefox',
            'version': '',
            'javascriptEnabled': True
        },
        browser_profile=fp
    )

    driver.get("http://gengo.com")
    elem = driver.find_element_by_id("translation")
    print driver.current_url
    print driver.title
    print elem.text
    driver.quit()
