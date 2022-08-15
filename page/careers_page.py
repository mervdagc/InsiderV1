
from selenium.webdriver.common.by import By
from base.base_function import *
from selenium.webdriver.support import expected_conditions as ec


class CareerPage:
    LOCATION_FIELDS = (By.XPATH, "//input[contains(@class, 'location')]")
    SEE_ALL_TEAMS_BUTTON = (By.LINK_TEXT, "See all teams")
    OUR_LOCATIONS = (By.XPATH, "//*[@id='career-our-location']")
    QA = (By.XPATH, "//h3[contains(text(),'Quality Assurance')]")
    FILTER_BY_LOCATION = (By.XPATH, "//span[@id='select2-filter-by-location-container']")
    SELECT_LOCATION = (By.XPATH, "//li[text()='Istanbul, Turkey']")
    FILTER_BY_DEPARTMENT = (By.XPATH, "//span[@id='select2-filter-by-department-container']")
    SELECT_DEPARTMENT = (By.XPATH, "//li[text()='Quality Assurance']")
    QA_JOB_LIST = (By.XPATH, "//div[@id='jobs-list']")
    TOTAL_QUERY_RESULT = (By.XPATH, "//span[@class='totalResult']")
    QUALITY_ASSURANCE = (By.XPATH, "//span[@class='position-department text-large font-weight-600 text-primary']['+x+']")




    def __init__(self,driver,explicit_wait=45):
        self.driver=driver


    def check(self):
        driver = self.driver
        wait = WebDriverWait(driver, 45)
        wait.until(ec.visibility_of_element_located(CareerPage.SEE_ALL_TEAMS_BUTTON), "Login page isn't visible!")

    def clickSeeAllTeamsButton(self):
        driver = self.driver
        WebDriverWait(driver, 45)
        element = self.driver.find_element(By.LINK_TEXT, "See all teams")
        driver.execute_script("arguments[0].click();", element)

    def selectQualityAssurance(self):
        driver = self.driver
        WebDriverWait(driver, 45)
        element = self.driver.find_element(By.XPATH, "//h3[contains(text(),'Quality Assurance')]")
        driver.execute_script("arguments[0].click();", element)

    def seeAllQAJobsButton(self):
        driver = self.driver
        WebDriverWait(driver, 45)
        element = self.driver.find_element(By.XPATH, "//a[contains(text(),'See all QA jobs')]")
        driver.execute_script("arguments[0].click();", element)

    def jobFilterByLocation(self):
        driver = self.driver
        wait = WebDriverWait(driver, 45)
        element1 = wait.until(ec.element_to_be_clickable(CareerPage.FILTER_BY_LOCATION),  "Bulunamadı")
        element1.click()
        element2 = wait.until(ec.element_to_be_clickable(CareerPage.SELECT_LOCATION),  "Bulunamadı")
        element2.click()

    def jobFilterByDepartment(self):
        driver = self.driver
        wait = WebDriverWait(driver, 45)
        element1 = wait.until(ec.element_to_be_clickable(CareerPage.FILTER_BY_DEPARTMENT),  "Bulunamadı")
        element1.click()
        element2 = wait.until(ec.element_to_be_clickable(CareerPage.SELECT_DEPARTMENT),  "Bulunamadı")
        element2.click()

    def checkQAJobList(self):
        driver = self.driver
        wait = WebDriverWait(driver, 45)
        totalQueryResult = wait.until(ec.presence_of_element_located(CareerPage.TOTAL_QUERY_RESULT), "Bulunamadı").text
        query = totalQueryResult.split(" ")
        for x in query:
            checkQa = wait.until(ec.presence_of_element_located(CareerPage.QUALITY_ASSURANCE), "").text
            print(checkQa)
            return checkQa
           # assertEquals(checkQa,"Quality Assurance")



















