from Utils.utils import Utils
import re
import datetime
from time import  sleep
import gc
from Utils.excel import Excel

class Alerts:
    
    util = Utils()

    def clickAlerts(self):
        self.util.clickElement('//*[@id="header_wrapper"]/nav[2]/ul/li[2]/a')

    def clickAllIncidents(self):
        self.util.clickElement('/html/body/div[1]/div/main/div[1]/incidents/div/div/div[1]/div[2]/a')

    def checkTitle(self, title, message):
        if self.util.getTitle() == title:
            self.util.setLog('Class: {0}, Option: {1}'.format(self.__class__.__name__, message))
            return True
        self.util.setLog('Something went wrong: {0}'.format(self.__class__.__name__)) 
        return False

    def searchIncidents(self, alert):
        self.util.setText('//input[@placeholder="Search incidents"]', alert)
    
    def cleanSearchIncident(self):
        self.util.cleanText('//input[@placeholder="Search incidents"]')

    def getAllIncidentsTable(self):
        return self.util.getAllItemsOfTable('//table[@class="dashboard zebra sort"]//tr')

    def nextPage(self):
        self.util.clickElement('//a[@class="next"]')

    
    def existsErrorsIncidents(self, list):
        correct_errors_list = []
        for log in list:
            for position, validate in enumerate(log):
                if validate == '-' or validate == '~' or validate == '':
                    log[position] = self.util.whatMonth(datetime.datetime.today().month)
                    
            correct_errors_list.append(log)

        gc.collect()
        return correct_errors_list, False      

    def stardardData(self, text):
        list = []
        new_list = []
        incidents_data = self.existsErrorsIncidents(text)

        if incidents_data[1] == False: # Get major frecuency from table
            for log in incidents_data[0]:
                time = (str(log[4]).split(' ')[0].split(':')[0])
                if time.isdigit() == True:
                    list.append(0)
                else:
                    list.append(time)

            frecuency_mode= self.util.whatMonth(datetime.datetime.today().month)
            list.clear()
            
            for log in incidents_data[0]: #Replace the value 0 to frecuecy result
                time = (str(log[4]).split(' ')[0].split(':')[0])
                if time.isdigit() == True:
                    list.append(frecuency_mode + ' ' +log[3])
                else:
                    list.append(log[3])

            for i, log in enumerate(incidents_data[0]): # Build the new structure
                log[3] = list[i]
                new_list.append(log)

        gc.collect()    
        return new_list
        

    def filterBy(self, month, list_elements):
        list = []
        list_tmp = []
        import re 
        try:
            for register in self.stardardData(list_elements):
                time = re.split("[A-z]+", register[-1])
                if len(time)==2: #Evaluate if is minute or hours
                    if not (int(time[0])<=2) == True: #Evaluate if minute is major to 2
                        list.append(register)
                else:
                    if not (int(time[0])<=0) == True: #Evaluate if hour is major to 0
                        list.append(register)
                        
            for item in list: #Evaluate if is Critical or Availability and save in list_tmp 
                if (item[1].split(' ')[3]+')') == '(Critical)' and item[3].split(' ')[0] == month:
                    item.append('Apdex_'+item[1].split(' ')[0])
                    list_tmp.append(item)
                else:
                    if item[1].split(' ')[0] == 'Ping' and (item[3].split(' ')[0]) == month:
                        item.append('Availability_'+item[1].split(' ')[3])
                        list_tmp.append(item)

            for item in list_tmp: #Clean data 
                item.pop(1)
                item.pop(1)
                item.pop(2)
            
            for value in list_tmp: #Build the new list
                time = value[1].split(',')
                duration = value[-2]
                type_incident = value[-1]
                value[1] = time[0]
                value[2] = time[1]
                value[3] = duration
                value.append(type_incident)
            
            return list_tmp

        except ValueError:
            print('Something went wrong')

           
    def viewAllIncidents(self):
        new_list = []
        self.clickAlerts()
        self.clickAllIncidents()
        self.checkTitle('Incidents - Alerts by New Relic', 'View All Incidents')

        filters = ['IB PROD', 'BM PROD', 'CTF PROD']
        list = []
        excel = Excel()

        for filter in filters:
            self.searchIncidents(filter)      
            for times in range(5):                
                results = (self.filterBy('Apr', self.getAllIncidentsTable()))
                if not (len(results) == 0) == True:
                    list.append(results)
              
                self.nextPage()
                self.cleanSearchIncident()
        for elements in list:
            for element in elements:
                new_list.append(element)
        
        if excel.createIncidentsReport(new_list) == True:                       
            self.util.setLog("Create Report, Result: Report created sucessfully")     
        else:
           self.util.setLog('Something went wrong: {0}, step: {1}'.format(self.__class__.__name__, 'Create Report'))  
                


        

