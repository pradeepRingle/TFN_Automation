from behave import when, given
from Locators import LoginPageLocators


@given(u"I go to the login page of the application")
def steps_impl(context):
    print("I am at Home Page")


@when(u"I enter {username} and {password}")
def steps_impl(context, username, password):
    context.lib.send_keyboard_keys(LoginPageLocators.email, username)
    context.lib.send_keyboard_keys(LoginPageLocators.password, password)


@when(u"I click login button")
def steps_impl(context):
    context.lib.click_event(LoginPageLocators.button)

