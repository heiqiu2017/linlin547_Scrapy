#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import requests,time,DUtils
from pyquery import PyQuery
class Utils_func:
    def __init__(self):
        self.driver = webdriver.PhantomJS(DUtils.PhantomJS_path)
    def selem_one_get(self,url):
        #首次获取页面源码
        self.driver.get(url)
        self.data = self.driver.page_source
        # self.driver.close()
        return self.data

    def req_get(self,url):
        #js页面无法获取源码
        self.r = requests.get(url,timeout=60)
        self.r.encoding = "utf-8"
        self.r.close()
        return self.r.text

    def query_body(self,body):
        return PyQuery(body)
    def quit_driver(self):
        self.driver.quit()