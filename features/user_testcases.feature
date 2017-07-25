Feature: User API testing
  As a tester, I want to verify all the APIs related to user are run as expected

  #HAPPY CASES

    #Get List User case
  @happy
  Scenario: Verify the list of user is return correctly by API
    When we GET the list of users at endpoint "/users"
    Then we receive a list JSON object contains 10 users

    #Search for a username case
  @happy
  Scenario Outline: Verify the API will response correct user when searching username using API
    When we GET a user with <username> at endpoint "/users?username="
    Then the user information in JSON object must have <name>,<email>,<website>
    Examples:
      | username | name             | email                    | website       |
      | Bret     | Leanne Graham    | Sincere@april.biz        | hildegard.org |
      | Kamren   | Chelsey Dietrich | Lucio_Hettinger@annie.ca | demarco.info  |
      | Delphine | Glenna Reichert  | Chaim_McDermott@dana.io  | conrad.com    |

    #Create a new user case
  @happy
  Scenario: Verify the a new user is created correctly by API
    Given there is an user information
      | username  | name | email         | website      |
      | viet pham | viet | viet@test.com | www.test.com |
    When we POST the user information at endpoint "/users"
    Then the new user must be created successfully

    #Update an existed-user
  @happy
  Scenario: Verify the user information is able to update correctly by API
    Given we want to update the user "Bret" with following information
      | name        | email                  | website           |
      | Bred Update | AnotherEmail@email.com | www.tryupdate.org |
    When we PUT the user update information at endpoint "/users/"
    Then the user must be updated successfully

    #Delete an exited-user
  @happy
  Scenario Outline: Verify that a user can be deleted by API
    Given we GET a user with <username> at endpoint "/users?username="
    When we DELETE the user at endpoint "/users/"
    Then the user must be deleted successfully
    Examples:
      | username      |
      | Bret          |
      | Elwyn.Skiles  |
      | Maxime_Nienow |


  #NEGATIVE CASES
  @negative
  Scenario Outline: Verify the API will not response any user when searching for invalid/non-existed username using API
    When we GET a user with <username> at endpoint "/users?username="
    Then the response must not contains any user result
    Examples:
      | username         |
      | blank            |
      | " "              |
      | number 999999999 |

