#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf-8')


class TestSampleSelenium(object):

    def setup(self):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", "en-us,en,ja")
        fp.update_preferences()

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={
                'platform': 'ANY',
                'browserName': 'firefox',
                'version': '',
                'javascriptEnabled': True
            },
            browser_profile=fp
        )

    def test_open_gengo(self):
        self.driver.get("http://gengo.com")
        elem = self.driver.find_element_by_id("translation")
        print self.driver.current_url
        print self.driver.title
        print "Judge: ", elem.text == "Order Translation"
        print "================================="
        print self.driver.page_source
        print "================================="

    def teardown(self):
        self.driver.quit()
