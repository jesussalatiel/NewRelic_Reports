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

    def searchIncidents(self, alert):
        self.util.setText('//input[@placeholder="Search incidents"]', alert)
    
    def cleanSearchIncident(self):
        self.util.cleanText('//input[@placeholder="Search incidents"]')

    def getAllIncidentsTable(self):
        return self.util.getAllItemsOfTable('//table[@class="dashboard zebra sort"]//tr')

    def nextPage(self):
        self.util.clickElement('//a[@class="next"]')

    def verifyTitleandSaveLog(self, title, message):
        if self.util.getTitle() == title:
            self.util.setLog('Class: {0}, Message: {1}'.format(self.__class__.__name__, message))

    def cleanListOfElements(self, list_incidents):
        
        def cleanListAnyElement():
            join_list = [] #Create a new list to save the new data  
            for _lists in list_incidents: #Separate the lists
                for position_list in _lists: #Show the elements of each list 
                    if not('-' in set(position_list)): #Comparate if any position of list is esqual '-', if is True, deleate position 
                        join_list.append(position_list) #Save a list elements without the following character '-' 
            return join_list #Return a list elements without the following character '-' 

        def fixTimesInList(join_list):
            import datetime #Import the library to get the days and moths
            x = datetime.datetime.now() #Get the time
            tmp_list = [] #Create list to save the new list
            for _list in join_list: #Show elements of the list
                if len(_list[3].split(',')) == 1: #If the len is esqual to 1 es because has the following structure '3:05 am' and we want the follwing structure 'Apr 24, 3:05 am'
                    time = x.strftime("%b")+' '+x.strftime("%d")+', '+_list[3] #We join %b = Month and %d = Day
                    _list[3] = time #Replace the data to the correct date
                    tmp_list.append(_list) #Save in the list 
                else: #If the len is equal to 2 is because has the following structure 'Apr 24, 3:05 am'
                    tmp_list.append(_list) 
            return tmp_list#Return the standard list
        
        return fixTimesInList(cleanListAnyElement()) #Return the list without errors

    def getApdexAndAvailabibility(self, select_month):
        import re
        monitors = ['IB PROD', 'BM PROD', 'CTF PROD'] #Monitors Name
        finally_list = [] #Save data to send to the final proccess
        results = [] #Save table data of the differents monitors
        times_to_get_data_of_the_tables = 8 #This variable is important "This define the coberture that has the month"
        for monitor in monitors: #Bucle to get the results of each monitor
            self.searchIncidents(monitor) #Search the name of the monitor
            for _ in range(0, times_to_get_data_of_the_tables): #How many time do you want get the data of each monitor
                results.append(self.getAllIncidentsTable()) #Save the incidents

                self.nextPage() #Pass to the next Page
                self.cleanSearchIncident() #Clean the input

        tpm_select_date = [] #Create list to save the new elements 
        for _list in self.cleanListOfElements(results): # Show the elements in the list 
            if str(_list[3].split(' ')[0]) == select_month: #Compare if it is equal to the month that the user chose
                tpm_select_date.append(_list) #Save the data with the user's month
      
        for _list in tpm_select_date: # Show the list to know if is apdex o available
            apdex = (_list[1].split(' ')[3])+')'  #Build the word (Critical)
            available = '('+(_list[1].split(' ')[0])+')' #Build the word (Ping)
          
            if apdex == '(Critical)': #Comparate if the name contains the word '(Critical)'
                name_monitor = 'Apdex_'+str(_list[1].split(' ')[0]) #Build the name for example 'Apdex_IB or Apdex_CTF'
                _list.append(name_monitor) #Add the name to final of the list to allows to make a classify
                finally_list.append(_list) #Add at the final list to can return it to the user 

            if available == '(Ping)': #Comparate if the name contains the word '(Ping)'
                name_monitor = 'Availability_'+_list[1].split(' ')[3]#Build the name for example 'Availability_IB or Availability_CTF'
                _list.append(name_monitor)#Add the name to final of the list to allows to make a classify
                finally_list.append(_list)#Add at the final list to can return it to the user 

        tpm_select_date.clear()#Clear list to free memory
        results.clear() #Clear list to free memory

        for _list in finally_list: #Show data to make corrections in the final output format
            correct_time =  (_list[3].split(',')) #Separate times
            _list[1] = str(correct_time[0]) #Date
            _list[2] = str(correct_time[1]) #Time
            _list.pop(3) #Remove the compleate date
            _list.pop(3) #Remove the close field
            format_time = (re.split("[A-z]+", _list[3])) 
            if len(format_time) == 3: #Are hours
                results.append(_list)
            if len(format_time) == 2: #Are minutes
                if int(format_time[0]) > 2: #If the time is major to 2 minutes, save in list
                    results.append(_list)

        finally_list.clear()#Clear list to free memory

        return results #Return Inicidents 
    
    def viewAllIncidents(self):
        self.clickAlerts()#Click on alerts
        self.clickAllIncidents()#Click on all incidents
        excel = Excel()#Instance the file
        if excel.createIncidentsReport(self.getApdexAndAvailabibility('Apr')) == True:
            self.verifyTitleandSaveLog('Incidents - Alerts by New Relic', 'Report created sucessfully')

            


            
           

        

