from selenium.webdriver.common.by import By


class ConfirmPage:

    # self.driver.find_element(By.ID, "country")
    # self.driver.find_element(By.LINK_TEXT, "India")
    # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    # self.driver.find_element(By.XPATH, "//input[@type='submit']")
    # self.driver.find_element(By.CLASS_NAME, "alert-success")
    Text = (By.ID, "country")
    Country = (By.LINK_TEXT, "India")
    Checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    FinalSubmitButton = (By.XPATH, "//input[@type='submit']")
    SuccessText = (By.CLASS_NAME, "alert-success")

    def __init__(self,driver):
        self.driver = driver

    def sendText(self):
        return self.driver.find_element(*ConfirmPage.Text)

    def countryOpted(self):
        return self.driver.find_element(*ConfirmPage.Country)

    def clickCheckbox(self):
        return self.driver.find_element(*ConfirmPage.Checkbox)

    def finalSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.FinalSubmitButton)

    def getSuccessText(self):
        return self.driver.find_element(*ConfirmPage.SuccessText)