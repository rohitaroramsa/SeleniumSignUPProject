
class signUp():
    def __init__(self , driver):
        self.driver = driver
        self.signupPage_class ='jnrGPE'
        self.username_id ='email'
        self.password_id ='password'
        self.acceptTerms_id ='terms'
        self.privacyPolicy_id ='consents'
        self.createAccount_class ='cqjiJV'
        self.error_text_class ='kPxmyV'

    def directToSignupPage(self):
        self.driver.find_element_by_class_name(self.signupPage_class).click()

    def set_username(self ,username):
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def set_password(self ,password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def acceptTerms(self):
        self.driver.find_element_by_id(self.acceptTerms_id).click()
        self.driver.find_element_by_id(self.acceptTerms_id).click()


    def acceptPrivacyPolicy(self):
        self.driver.find_element_by_id(self.privacyPolicy_id).click()

    def createAccount(self):
        self.driver.find_element_by_class_name(self.createAccount_class).click()

    def getError(self):
        return self.driver.find_element_by_class_name(self.error_text_class).text
