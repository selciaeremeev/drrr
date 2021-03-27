#!/usr/bin/env python
# coding: utf-8
""" POM class for Entrance """
from typing import List

from selenium.webdriver.remote.webelement import WebElement

from base.base import Base


class Entrance(Base):
    """ POM class for Entrance """

    @property
    def room_list(self) -> List[WebElement]:
        """ Return Room list """
        return self.driver.find_element_by_id("room_list").find_elements_by_class_name("rooms.clearfix")
