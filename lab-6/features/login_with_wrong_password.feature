Feature: Login with wrong password

  As a user,
  I want to see an error message when I login with wrong password,
  So I know that I used the wrong password.

  Scenario: Login with wrong password in Firefox browser
    Given Firefox browser opened
    When navigate to 'https://practicetestautomation.com/practice-test-login'
    And enter login 'student'
    But enter password 'wrong_password'
    And click submit button
    Then wrong password error message is displayed
    And browser is closed

  Scenario: Login with wrong password in Chrome browser
    Given Chrome browser opened
    When navigate to 'https://practicetestautomation.com/practice-test-login'
    And enter login 'student'
    But enter password 'wrong_password'
    And click submit button
    Then wrong password error message is displayed
    And browser is closed
