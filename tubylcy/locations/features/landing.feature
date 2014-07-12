Feature: Main Page

    Background:
        Given a browser

    Scenario: Search for BDD
        When I visit "http://127.0.0.1:8000/"
        Then browser title is "Help Your Community"