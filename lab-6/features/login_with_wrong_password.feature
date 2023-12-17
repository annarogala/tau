Feature: Login with wrong password

  As a user,
  I want to see an error message when I login with wrong password,
  So I know that I used the wrong password.

.
  Scenario: Login with wrong password in Firefox browser
    Given Firefox browser opened
    When navigate to 'https://practicetestautomation.com/practice-test-login'
    When enter login 'student'
    When enter password 'wrong_password'
    When click submit button
    Then wrong password error message is displayed
    Then browser is closed

  Scenario: Login with wrong password in Chrome browser
    Given Chrome browser opened
    When navigate to 'https://practicetestautomation.com/practice-test-login'
    When enter login 'student'
    When enter password 'wrong_password'
    When click submit button
    Then wrong password error message is displayed
    Then browser is closed
