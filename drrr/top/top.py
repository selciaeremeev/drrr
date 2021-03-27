#!/usr/bin/env python
# coding: utf-8
""" POM class for Top """
from typing import List

from selenium.webdriver.remote.webelement import WebElement

from base.base import Base


class Top(Base):
    """ POM class for Top """

    @property
    def icons(self) -> List[WebElement]:
        """ Return Icons list """
        return self.driver.find_element_by_class_name("icons").find_elements_by_tag_name("li")
    
    @property
    def user_name(self) -> WebElement:
        """ Returns UserName WebElement """
        return self.driver.find_element_by_id("name")

    @property
    def login(self) -> WebElement:
        """ Return Login WebElement """
        return self.driver.find_element_by_class_name("bb.cc")
