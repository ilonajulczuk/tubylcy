from behaving.web.steps import *
from behaving import environment as benv


def before_scenario(context, scenario):
    benv.before_scenario(context, scenario)


def after_scenario(context, scenario):
    context.browser.driver.close()