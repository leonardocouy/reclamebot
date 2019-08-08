# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ReclamebotSpider(scrapy.Spider):
    name = 'reclamebot'
    allowed_domains = ['reclameaqui.com.br']
    start_urls = ['https://www.reclameaqui.com.br/']

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')

        self.driver = webdriver.Chrome(chrome_options=options)

    def parse(self, response):
        self.log('visitei a página de login: {}'.format(response.url))
        try:
            self.driver.get(response.url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@id='btn-signIn-header']"))
            )
            next = self.driver.find_element_by_xpath('//a[@id="btn-signIn-header"]')
            next.click()
            yield scrapy.Request(response.url, callback=self.parse2)
        except:
            self.log("deu ruim!")

        self.driver.close()

    def parse2(self, response):
        print(response)