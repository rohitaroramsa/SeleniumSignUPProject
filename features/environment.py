from behave import fixture
from selenium import webdriver

'''driver path for chrome Brwosert'''
chrome_driver_path = 'C:\\WS\\TypeForm\\chromedriver.exe'

url='https://admin.typeform.com/login/'

# -- FIXTURE- To pass Browser Driver to features
@fixture
def get_browser(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(chrome_driver_path, options=options)
    context.driver.implicitly_wait(15)
    context.driver.get(url)
    context.driver.find_element_by_class_name('accept-cookies-button').click()  #Accept Cookies on UI
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver.close()