from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Utils:

    driver = webdriver.Chrome('../chromedriver.exe') #Instance webdriver

    def setupBrowser(self, URL):
        self.driver.get(URL) #Access to the website
        self.driver.delete_all_cookies() #Clean all cookies

    def clickElement(self, xpath):
        element = self.waitForElement(xpath) #Wait for the presence of a element
        element.click() #Click on the button

    def setText(self, xpath, text):
        input = self.waitForElement(xpath)#Wait for the presence of a element
        input.send_keys(text) #Set text to input

    def cleanText(self, xpath):
        input = self.waitForElement(xpath).clear() #Clear input

    def waitForElement(self, xpath):
        wait_time_request = 100 #This method waiting for a presence of a element on the web page its predetermined time is 100 miliseconds
        element = WebDriverWait(self.driver, wait_time_request).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element #Return web element

    def getAllItemsOfTable(self, xpath):
        elements_list = [] #Create list to save all the elements
        sleep(1)  # Wait 1 second
        table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )

        for table_elements in table: #Iterate in the table 
            text = (table_elements.text).split('\n') #Separate the chain from the elements because these elements are coming together
            elements_list.append(text)  # Save tables values

        elements_list.pop(0)  # Clean titles from table
        return elements_list #Return list with separate elemets

    def getTitle(self):
        return self.driver.title #Return the title

    def setLog(self, text): #Create the log message to display on the console
        executor_url = self.driver.command_executor._url #Get the machine when is it executing the test
        session_id = self.driver.session_id #Get the session id
        title_page = self.driver.title #Get the title
        '''Create Message'''
        report = "\n------------- Title Page: {0} --------------\n".format(title_page)
        report += "Executor URL: {0},\nSession ID: {1},\nStep: {2}.".format(executor_url, session_id, text)
        report += "\n_____________________________________________________________________"
        print(report)#Print Message

