Feature: Login with wrong username

  As a user,
  I want to see an error message when I login with wrong username,
  So I know that I used the wrong username.

  Scenario: Login with wrong username in Firefox browser
    Given Firefox browser opened
    When navigate to 'https://practicetestautomation.com/practice-test-login'
    When enter login 'wrong_username'
    When enter password 'Password123'
    When click submit button
    Then wrong username error message is displayed
    Then browser is closed

  Scenario: Login with wrong username in Chrome browser
    Given Chrome browser opened
    When navigate to 'https://practicetestautomation.com/practice-test-login'
    When enter login 'wrong_username'
    When enter password 'Password123'
    When click submit button
    Then wrong username error message is displayed
    Then browser is closed
