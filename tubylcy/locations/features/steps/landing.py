from behave import *


@then('browser title is "Help Your Community"')
def steps_impl(context):
    assert context.browser.title ==  'Help your community'