Feature: Landing

    Background:
        Given a browser

    Scenario: Search for BDD
        When I visit "http://localhost:8081/"
        Then browser title is "Help your community"
        And then I should see "Choose your adventure!"
        And then I should see "Mark your places of interest"