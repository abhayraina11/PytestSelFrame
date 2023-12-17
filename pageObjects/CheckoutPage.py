from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    # self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")
    # self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-success')]")
    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut = (By.XPATH, "//button[contains(@class,'btn-success')]")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def clickCheckoutButton(self):
        return self.driver.find_element(*CheckOutPage.checkoutButton)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
