from behave import given, when, then, use_fixture
from pages.signUpPage import signUp
from features.environment import get_browser
import time


@given(u'Chrome Browser')
def step_impl(context):
    context.driver = use_fixture(get_browser, context)
    context.page = signUp(context.driver)



@when(u'clicks on Signup button')
def step_impl(context):
    context.page.directToSignupPage()


@when(u'Provides a username')
def step_impl(context):
    context.page.set_username('rohit.arora.msa@gmail.com')


@when(u'Provides a password')
def step_impl(context):
    context.page.set_password('somewhere')


@when(u'Accepts Terms of Services')
def step_impl(context):
    context.page.acceptTerms()



@when(u'Accepts Privacy Policy')
def step_impl(context):
    context.page.acceptPrivacyPolicy()


@when(u'clicks On Create My Free Account Button')
def step_impl(context):
    context.page.createAccount()
    time.sleep(10)


@then(u'Account should be created')
def step_impl(context):
    pass

@then(u'should get an error to accept Terms')
def step(context):
    expected_error_value = '''You need to accept our Terms of Service and Privacy Policy to create a Typeform account. See options to change your preferences'''
    error_on_ui = context.page.getError()
    assert error_on_ui == expected_error_value