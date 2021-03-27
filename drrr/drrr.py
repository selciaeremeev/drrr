#!/usr/bin/env python
# coding: utf-8
""" Application class for Drrr """
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from top.top import Top


class Drrr:
    """ Application class for Drrr """

    def __init__(self) -> None:
        self.driver: WebDriver = webdriver.Chrome()

    @property
    def top(self) -> Top:
        """ Return Top instance """
        return Top(self.driver)

    def open(self) -> None:
        """ Open drrr """
        self.driver.get("http://drrrkari.com/")

    def close(self) -> None:
        """ Close drrr """
        self.driver.quit()
