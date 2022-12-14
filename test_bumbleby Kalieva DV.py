# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBumbleby():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_bumbleby(self):
    self.driver.get("https://qa.neapro.site/login/")
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("dinarakalieva021289@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("10101104")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active .document-tile:nth-child(1) > .document-name").click()
    self.driver.find_element(By.ID, "surname").click()
    self.driver.find_element(By.ID, "surname").send_keys("Кали")
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Дин")
    self.driver.find_element(By.ID, "patronymic").click()
    self.driver.find_element(By.ID, "patronymic").send_keys("Вал")
    self.driver.find_element(By.NAME, "date").click()
    self.driver.find_element(By.NAME, "date").send_keys("02.12.1989")
    self.driver.find_element(By.ID, "passportSeries").click()
    self.driver.find_element(By.ID, "passportSeries").send_keys("1122")
    self.driver.find_element(By.ID, "passportNumber").click()
    self.driver.find_element(By.ID, "passportNumber").send_keys("123456")
    self.driver.find_element(By.CSS_SELECTOR, "#dateOfIssue .mx-input").click()
    self.driver.find_element(By.CSS_SELECTOR, "#dateOfIssue .mx-input").send_keys("04.12.2009")
    self.driver.find_element(By.ID, "code").click()
    self.driver.find_element(By.ID, "code").send_keys("007001")
    self.driver.find_element(By.ID, "cardId").click()
    self.driver.find_element(By.ID, "cardId").send_keys("11122233344")
    self.driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").click()
    self.driver.find_element(By.ID, "issued").send_keys("ТП УФМС")
    self.driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("г Москва Хорошевское шоссе, д 1")
    self.driver.find_element(By.CSS_SELECTOR, ".vue-dadata__suggestions-item").click()
    self.driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").click()
    self.driver.find_element(By.ID, "phone").click()
    self.driver.find_element(By.ID, "phone").send_keys("9266590201")
    self.driver.find_element(By.CSS_SELECTOR, ".outline").click()
    self.driver.find_element(By.XPATH, "//input[@type=\'file\']").send_keys("C:\\Test\\Passport\\1.jpg")
    time.sleep(3)
    self.driver.find_element(By.CSS_SELECTOR, ".fill").click()
  
