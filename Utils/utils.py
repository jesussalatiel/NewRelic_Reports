from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Utils:

    driver = webdriver.Chrome('../chromedriver.exe')

    def setupBrowser(self, URL):
        self.driver.get(URL)
        self.driver.delete_all_cookies()
        # self.driver.maximize_window()

    def clickElement(self, xpath):
        element = self.waitForElement(xpath)
        element.click()

    def setText(self, xpath, text):
        input = self.waitForElement(xpath)
        input.send_keys(text)

    def cleanText(self, xpath):
        input = self.waitForElement(xpath).clear()

    def waitForElement(self, xpath):
        wait_time_request = 100
        element = WebDriverWait(self.driver, wait_time_request).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element

    def getAllItemsOfTable(self, xpath):
        elements_list = []
        sleep(1)  # Wait 1 second
        table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )

        for table_elements in table:
            text = (table_elements.text).split('\n')
            elements_list.append(text)  # Save tables values

        elements_list.pop(0)  # Deleate titles from table
        return elements_list

    def whatMonth(self, month):
        number = {
            1: 'Jan',
            2: 'Feb',
            3: 'Mar',
            4: 'Apr',
            5: 'May',
            6: 'Jun',
            7: 'Jul',
            8: 'Aug',
            9: 'Sep',
            10: 'Oct',
            11: 'Nov',
            12: 'Dec'
        }

        return number.get(month)

    def typeErrors(self, position):
        type_incident = {
            0: 'ID',
            1: 'Name',
            2: 'Open Violations',
            3: 'Opened',
            4: 'Closed',
            5: 'Duration'
        }
        return type_incident.get(position)

    def getTitle(self):
        return self.driver.title

    def setLog(self, text):
        executor_url = self.driver.command_executor._url
        session_id = self.driver.session_id
        title_page = self.driver.title
        report = "\n__________________________________________________________________\n"
        report += "Executor URL: {0},\nSession ID: {1},\nTitle Page: {2},\nStep: {3}.".format(
            executor_url, session_id, title_page, text)
        report += "\n__________________________________________________________________\n"

        print(report)

