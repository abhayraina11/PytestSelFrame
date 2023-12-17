import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Firstname is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getPassword().send_keys("pass@123")
        self.selectOptionByText(homepage.selectGender(), getData["gender"])
        homepage.selectCheckbox().click()
        homepage.clickSubmission().click()
        msg = homepage.getTextDisplayed().text
        print(msg)
        assert "Success!" in msg
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param