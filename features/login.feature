Feature: Users with correct credentials should be able to login and invalid credentials should be rejected

  Scenario: Users with correct credentials should be able to login
    Given Chrome browser has opened Login Page
    When User enters valid username "rohit.arora.msa@gmail.com"
      And User enters valid password "something"
      And User clicks on Login Button
    Then User login shoudl be successful

  Scenario: User with wrong credential should get error
    Given Chrome browser has opened Login Page
    When User enters valid username "dontexist@gmail.com"
      And User enters valid password "wrondpswd"
      And User clicks on Login Button
    Then User should get an error
