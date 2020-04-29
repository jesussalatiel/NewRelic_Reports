try:
    from Methods.Login import Login
    from Methods.Alerts import Alerts
    from credentials import data_credentials

    '''Start Login'''
    login = Login(data_credentials['url'], data_credentials['user'], data_credentials['password']) #Get credentials data of the dictionary
    login.startLogin()

    '''Create Alert Report'''
    alerts = Alerts()
    alerts.viewAllIncidents()

except:
    import sys
    print("Something went wrong: {0}".format(sys.exc_info()[0]))
finally:
    login.logOut()

