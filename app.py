
from Methods.Login import Login
from Methods.Alerts import Alerts

URL = 'https://newrelic.com/'
user = ''
password = ''

login = Login(URL, user, password)
login.startLogin()

alerts = Alerts()
alerts.viewAllIncidents()
