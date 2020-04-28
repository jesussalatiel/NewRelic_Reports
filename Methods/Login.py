from Utils.utils import Utils
class Login:

    user = None
    password = None
    
    def __init__(self, URL, user, password):
        self.util = Utils()
        self.util.setupBrowser(URL)
        self.user = user
        self.password = password

    def clickLogIn(self):
        self.util.clickElement('//*[@id="desk-login"]/span')
    
    def setUser(self, user):
        self.util.setText('//input[@id="login_email"]', user)
    
    def setPassword(self, password):
        self.util.setText('//input[@id="login_password"]', password)
    
    def clickSignIn(self):
        self.util.clickElement('//input[@id="login_submit"]')
    
    def logOut(self):
        self.util.driver.quit()

    def verifyTitleandSaveLog(self, title, message):
        self.util.setLog('Class: {0}, Message: {1}'.format(self.__class__.__name__, message))

    def startLogin(self):
        self.clickLogIn()
        self.setUser(self.user)
        self.setPassword(self.password)
        self.clickSignIn()
        self.verifyTitleandSaveLog('All applications - New Relic', 'Session Started')
            
        
            

        