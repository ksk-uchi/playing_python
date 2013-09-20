#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://www.google.com")
    elem = driver.find_element_by_id("hplogo")
    print elem.get_attribute("title")
    driver.quit()
