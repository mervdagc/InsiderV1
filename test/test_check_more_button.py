import time

from Utilities.BaseClass import BaseClass
import page.home_page
import page.careers_page


class Test_All(BaseClass):
    department = "Quality Assurance"

    def testAll(self):
        homepage = page.home_page.HomePage
        homepage.close_cookies(self)
        homepage.clickMoreButton(self)
        time.sleep(1)
        homepage.clickCareersButton(self)
        careerpage = page.careers_page.CareerPage
        careerpage.clickSeeAllTeamsButton(self)
        careerpage.selectQualityAssurance(self)
        careerpage.seeAllQAJobsButton(self)
        time.sleep(2)
        careerpage.jobFilterByLocation(self)
        careerpage.jobFilterByDepartment(self)
        careerpage.checkQAJobList(self)





        time.sleep(5)






# import time
#
# from selenium import webdriver
# from base.base_test import BaseTest
# from page.home_page import HomePage
# from page.careers_page import CareerPage
#
# from base.base_function import Base
# from selenium.webdriver.support import  expected_conditions as ec
#
#
# class testCheckMoreButton(BaseTest):
#
#
#
#
#      def webTestMoreButton(self):
#         homepage=HomePage(self.driver)
#         homepage.clickMoreButton()
#         homepage.clickCareersButton()
#         time.sleep(2)
#
#         careerpage=CareerPage(self.driver)
#
#      if __name__ == "__main__":
#          BaseTest()
#          webTestMoreButton()
#
#
#      def tearDown(self):
#          Base.quit_driver(self)



