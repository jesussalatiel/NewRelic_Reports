from Utils.utils import Utils

class Monitor:

    util = Utils()

    def verifyAPMMonitor(self):
        health_status = ['health-status red', 'health-status green', 'health-status yellow', 'health-status gray'] #Declare Status 
        monitor_name= ['BM Prod', 'IB Prod', 'CTF Prod'] #Declare Monitors
        class_attribute, other_attribute = (self.util.getAllItemsOfTableByAttribute('//table[@class="agent_summary_table tablesorter"]//td/a', 'class'))  #Get elements of the table by class  
        _name=[] #Declare variables to build the word 
        _monitor=[]#Declare variables to build the word 

        for monitor, other in zip(class_attribute, other_attribute): #Show the lists the first return status color and second return its properties

            if (other in monitor_name): #Verify if exists the 'BM Prod' in the list name_monitor and print monitor and assign the monitor name
                _name.append(other)
            if (monitor in health_status): #Verify if exists the 'health-status green' in the list health_status and assign the color status
                _monitor.append(monitor)

        list = (set(zip(_name, _monitor))) #Convert elements to list
        message= 'Verify APM Monitors\n'#Declare variable to save message

        for i in list: #Show elemets of the list to know its status
            if 'health-status gray' in i:
                message += ('Error: Monitor {0} has is not reporting has a status {1}.\n'.format(i[0],i[1].split(' ')[1]))
            elif 'health-status red' in i:
                message+=('Warning: Monitor {0} is reporting status {1}.\n'.format(i[0],i[1].split(' ')[1]))
            elif 'health-status green' in i:
                message+=('Great: Monitor {0} is reporting sucessfully status {1}.\n'.format(i[0],i[1].split(' ')[1]))

        self.util.setLog(message) #Show log message