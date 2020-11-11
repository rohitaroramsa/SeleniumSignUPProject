from behave import given, when, then, use_fixture
from pages.loginPage import loginPage
from features.environment import get_browser
import time


@given(u'Chrome browser has opened Login Page')
def step_impl(context):
    context.driver = use_fixture(get_browser, context)
    context.page = loginPage(context.driver)


@when(u'User enters valid username "{username}"')
def step_impl(context,username):
    context.page.setUserName(username)


@when(u'User enters valid password "{password}"')
def step_impl(context,password):
    context.page.setPassword(password)


@when(u'User clicks on Login Button')
def step_impl(context):
    context.page.clickLogin()
    time.sleep(2)


@then(u'User login shoudl be successful')
def step_impl(context):
    pass

@then(u'User should get an error')
def step(context):
    expected_error_value = '''Your login info isn't right. Try again, or reset your password if it slipped your mind.'''
    error_on_ui = context.page.getError()
    assert error_on_ui == expected_error_value
