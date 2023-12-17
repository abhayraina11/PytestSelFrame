from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage
class HomePage:

    def __init__(self,driver):
        self.driver = driver

    # find_element(By.NAME,"name").send_keys("Abhay")
    # driver.find_element(By.NAME, "email").send_keys("rahulshettyacademy.com")
    # driver.find_element(By.CSS_SELECTOR,"#exampleInputPassword1").send_keys("pass@123")
    # driver.find_element(By.ID,"exampleFormControlSelect1")
    # driver.find_element(By.ID, "exampleCheck1").click()
    # driver.find_element(By.XPATH, "//input[@type='submit']").click()
    # driver.find_element(By.CLASS_NAME, "alert")
    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.CSS_SELECTOR, "#exampleInputPassword1")
    gender = (By.ID, "exampleFormControlSelect1")
    checkbox = (By.ID, "exampleCheck1")
    submission = (By.XPATH, "//input[@type='submit']")
    alertmsg = (By.CLASS_NAME, "alert")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def selectGender(self):
        return self.driver.find_element(*HomePage.gender)

    def selectCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def clickSubmission(self):
        return self.driver.find_element(*HomePage.submission)

    def getTextDisplayed(self):
        return self.driver.find_element(*HomePage.alertmsg)