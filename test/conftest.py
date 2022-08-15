
import pytest



from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver_path = "/Users/mrvdgc/PycharmProjects/UseInsedirV2/base/webdrivers/chromedriverMac64"
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get("https://useinsider.com/")
    driver.implicitly_wait(7)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


    # def __init__(self):
    #     self.driver = webdriver.Chrome("/Users/mrvdgc/PycharmProjects/UseInsedirV2/base/webdrivers/chromedriverMac64")
    #     self.driver.get("https://useinsider.com/")
    #     self.driver.maximize_window()
    #
    #     time.sleep(2)
    #
    # def drivertest(self):
    #     time.sleep(2)

