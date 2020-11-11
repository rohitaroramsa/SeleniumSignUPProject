Feature: New User should be able to signup to TypeForm if all inputs are correct

Scenario: New user wish to signup should be able to successfully signed up
  Given Chrome Browser
  When clicks on Signup button
    And Provides a username
    And Provides a password
    And Accepts Terms of Services
    And Accepts Privacy Policy
    And clicks On Create My Free Account Button
  Then Account should be created

Scenario: New user who wish to signup must accepts Terms and condition
  Given Chrome Browser
  When clicks on Signup button
    And Provides a username
    And Provides a password
    And Accepts Privacy Policy
    And clicks On Create My Free Account Button
  Then should get an error to accept Terms