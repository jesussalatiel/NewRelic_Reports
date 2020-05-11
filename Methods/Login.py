from Utils.utils import Utils

class Login:
        
    def __init__(self, URL, user, password):
        self.util = Utils()
        self.util.setupBrowser(URL) #Clean cookies and go to the web page
        self.user = user #Initialize user variable
        self.password = password #Initialize password variable

    def clickLogIn(self):
        self.util.clickElement('//*[@id="desk-login"]/span')
    
    def setUser(self, user):
        self.util.setText('//input[@id="login_email"]', user)
    
    def setPassword(self, password):
        self.util.setText('//input[@id="login_password"]', password)
    
    def clickSignIn(self):
        self.util.clickElement('//input[@id="login_submit"]')
    
    def logOut(self):
        self.util.setLog('Class: {0}, Message: {1}'.format(self.__class__.__name__, 'Session Finished'))
        self.util.driver.close()

    def verifyTitleandSaveLog(self, title, message):
        self.util.setLog('Class: {0}, Message: {1}'.format(self.__class__.__name__, message))
    
    def saveCookies(self):
        pass
    
    def startLogin(self):
        self.clickLogIn() #Click ok Login
        self.setUser(self.user) #Write User on the texbox
        self.setPassword(self.password)#Write Password on the texbox
        self.clickSignIn()#CLick ok Signin
        self.verifyTitleandSaveLog('All applications - New Relic', 'Session Started')#Verify the title
            
        
            

        