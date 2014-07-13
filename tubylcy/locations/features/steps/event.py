from behaving.web.steps import *

@when('I log in EVI')
def log_in(context):
    assert context.configuration
    context.execute_steps(u"""
        When I visit "{0}"
        And I fill in "username" with "{1}"
        And I fill in "password" with "{2}"
        And I press the element with xpath "//*[@type='submit']"
        Then I should see "DOD Monitoring Consent" within 5 seconds
        And I press "Accept"
    """.format(context.configuration['login_url'], context.configuration['username'], context.configuration['password']))
