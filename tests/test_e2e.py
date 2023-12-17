import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("Successfully Getting all the card titles")
        products = checkOutPage.getCardTitles()
        for product in products:
            productName = product.find_element(By.XPATH, "div/p").text
            log.info(productName)
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
        checkOutPage.clickCheckoutButton().click()
        confirmPage = checkOutPage.checkOutItems()
        log.info("Entering country name as IND")
        confirmPage.sendText().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmPage.countryOpted().click()
        confirmPage.clickCheckbox().click()
        confirmPage.finalSubmitButton().click()
        message = confirmPage.getSuccessText().text
        log.info("Text received from application is"+message)
        assert "Success! Thank you!" in message



