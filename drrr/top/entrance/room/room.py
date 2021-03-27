#!/usr/bin/env python
# coding: utf-8
""" POM class for Room """
from typing import List

from selenium.webdriver.remote.webelement import WebElement

from base.base import Base


class Room(Base):
    """ POM class for Room """

    @property
    def leave(self) -> WebElement:
        """ Return leave WebElement """
        return self.driver.find_element_by_name("logout")

    @property
    def message(self) -> WebElement:
        """ Return message WebElement """
        return self.driver.find_element_by_name("message")

    @property
    def post(self) -> WebElement:
        """ Return post WebElement """
        return self.driver.find_element_by_name("post")

    @property
    def bubble(self) -> List[WebElement]:
        """ Return bubble WebElement """
        return self.driver.find_elements_by_class_name("bubble")
