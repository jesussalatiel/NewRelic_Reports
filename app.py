try:
    from Methods.Login import Login
    from Methods.Alerts import Alerts
    from Methods.Monitor import Monitor
    from Methods.Daily_Report import Daily_Report
    from credentials import data_credentials

    '''Start Login'''
    login = Login(data_credentials['url'], data_credentials['user'], data_credentials['password']) #Get credentials data of the dictionary
    login.startLogin()

    '''Verify Health Status Monitors'''
    monitor = Monitor()
    monitor.verifyAPMMonitor()

    '''Create Alert Report'''
    alerts = Alerts()
    alerts.viewAllIncidents()

    '''Build a document to send to the client'''
    #daily_report = Daily_Report()
    #daily_report.buildReport()
    
except:
    import sys
    print("Something went wrong: {0}".format(sys.exc_info()[0]))
finally:
    login.logOut()

