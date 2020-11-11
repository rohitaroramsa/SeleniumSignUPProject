class loginPage():

    def __init__(self,driver):
        self.driver = driver
        self.username_text_id = 'email'
        self.password_text_id = 'password'
        self.login_btn_id = 'btnlogin'
        self.error = 'eZOJQb'

    def setUserName(self,username):
        self.driver.find_element_by_id(self.username_text_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.password_text_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.login_btn_id).click()

    def getError(self):
        return self.driver.find_element_by_class_name(self.login_btn_id).text