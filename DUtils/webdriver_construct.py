# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import DUtils

class Info_Driver:
    def __init__(self,driver_name):
        if driver_name.lower() == "phantomjs":
            self.driver = webdriver.PhantomJS(DUtils.PhantomJS_path)
        elif driver_name.lower() == "chrome":
            self.driver = webdriver.Chrome(executable_path=DUtils.Chrome_path)
    def get_driver(self):
        return self.driver
    def wait_id(self,id,num=None):
        if num:
            return WebDriverWait(self.driver, 30, poll_frequency=2).until(lambda x: x.find_elements_by_id(id))
        else:
            return WebDriverWait(self.driver,30, poll_frequency=2).until(lambda x: x.find_element_by_id(id))
    def wait_name(self,name,num=None):
        if num:
            return WebDriverWait(self.driver, 30, poll_frequency=2).until(lambda x: x.find_elements_by_name(name))
        else:
            return WebDriverWait(self.driver,30, poll_frequency=2).until(lambda x: x.find_element_by_name(name))
    def wait_class_name(self,class_name,num=None):
        if num:
            return WebDriverWait(self.driver, 30, poll_frequency=2).until(lambda x: x.find_elements_by_class_name(class_name))
        else:
            return WebDriverWait(self.driver,30, poll_frequency=2).until(lambda x: x.find_element_by_class_name(class_name))
    def wait_css(self,css,num=None):
        if num:
            return WebDriverWait(self.driver, 30, poll_frequency=2).until(lambda x: x.find_elements_by_css_selector(css))
        else:
            return WebDriverWait(self.driver,30, poll_frequency=2).until(lambda x: x.find_element_by_css_selector(css))
    def wait_tag_name(self,tag_name,num=None):
        if num:
            return WebDriverWait(self.driver, 30, poll_frequency=2).until(lambda x: x.find_elements_by_tag_name(tag_name))
        else:
            return WebDriverWait(self.driver,30, poll_frequency=2).until(lambda x: x.find_element_by_tag_name(tag_name))
    def wait_xpath(self,xpath,num=None):
        if num:
            return WebDriverWait(self.driver, 30, poll_frequency=2).until(lambda x: self.driver.find_elements_by_xpath(xpath))
        else:
            return WebDriverWait(self.driver,30, poll_frequency=2).until(lambda x: self.driver.find_element_by_xpath(xpath))
    def wait_text(self,text,num=None):
        if num:
            return WebDriverWait(self.driver, 30, poll_frequency=2).until(lambda x: x.find_elements_by_link_text(text))
        else:
            return WebDriverWait(self.driver,30, poll_frequency=2).until(lambda x: x.find_element_by_link_text(text))
    def wait_partial_text(self,partial_text,num=None):
        if num:
            return WebDriverWait(self.driver, 30, poll_frequency=2).until(lambda x: x.find_element_by_partial_link_text(partial_text))
        else:
            return WebDriverWait(self.driver,30, poll_frequency=2).until(lambda x: x.find_element_by_partial_link_text(partial_text))
    def quit_close(self):
        self.driver.close()
    def quit_driver(self):
        self.driver.quit()