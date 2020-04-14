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
        self.util.clickElement('//*[@id="account_nav"]')
        self.util.clickElement('//a[@ng-click="logout()"]')
        self.util.setLog('Class: {0}, Message: Sucessful Logout'.format(self.__class__.__name__))

    def verifyTitleandSaveLog(self, title, message):
        if self.util.getTitle() == title:
            self.util.setLog('Class: {0}, Message: {1}'.format(self.__class__.__name__, message))
            return True
        self.util.setLog('Something went wrong: {0}'.format(self.__class__.__name__)) 
        return False

    def startLogin(self):
        self.clickLogIn()
        self.setUser(self.user)
        self.setPassword(self.password)
        self.clickSignIn()
        self.verifyTitleandSaveLog('All applications - New Relic', 'Session Started')
            
        
            

        