Feature: Main Page

    Background:
        Given a browser

    Scenario: Search for BDD
        When I visit "http://localhost:8081/"
        Then browser title is "Help your community"