from behave import *


@when('browser title is "Help Your Community"')
def steps_impl(context):
    assert context.browser.title ==  'Help Your Community'