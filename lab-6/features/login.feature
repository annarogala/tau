Feature: Login success

  As a user,
  I want to login to Practice Test Automation portal,
  So that I can access the test features.

  Scenario: Login successfully in Firefox browser
    Given Firefox browser opened
    When navigate to 'https://practicetestautomation.com/practice-test-login'
    When enter login 'student'
    When enter password 'Password123'
    When click submit button
    Then redirect to 'https://practicetestautomation.com/logged-in-successfully/'
    Then successfully logged in message is displayed
    Then browser is closed

  Scenario: Login successfully in Chrome browser
    Given Chrome browser opened
    When navigate to 'https://practicetestautomation.com/practice-test-login'
    When enter login 'student'
    When enter password 'Password123'
    When click submit button
    Then redirect to 'https://practicetestautomation.com/logged-in-successfully/'
    Then successfully logged in message is displayed
    Then browser is closed
