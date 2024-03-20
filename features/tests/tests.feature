Feature: Test Scenarios for Reelly

  @smoke
  Scenario: User is able to login to Reelly
    Given I use browser options: chrome headless
    Given I navigate to: https://soft.reelly.io/sign-in
    When I input username: nboulatov@gmail.com
    When I input password: 123
    When I click button: Continue
    Then I verify page is displayed: Main Page

  Scenario Outline: User is able to see social media icons
    Given I use browser options: <browser> <headless_or_not>
    Given I navigate to: https://soft.reelly.io/sign-in
    When I input username: nboulatov@gmail.com
    When I input password: 123
    When I click button: Continue
    When I click Menu Block button: Settings
    Then I see URL contains text: Settings
    When I click on button: Contact us
    Then I see URL contains text: contact-us
    Then I verify number of social media icons: 4

    Examples:
      | browser | headless_or_not |
      | firefox | headless        |
      | firefox |                 |
      | chrome  | headless        |
      | chrome  |                 |
