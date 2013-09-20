#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver


print "start"

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://www.google.com")
    elem = driver.find_element_by_id("hplogo")
    if elem.get_attribute("title") == "Google":
        pass
    else:
        raise AssertionError("poor.")
    driver.quit()
