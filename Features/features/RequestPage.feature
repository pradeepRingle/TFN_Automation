Feature: Request Feature

  @Create
  Scenario: Verify the user is able to create a New Request
    Given I go to the login page of the application
    When I enter tfn.req2020@gmail.com and Requestor1!
    And I click login button
    Then I am on the home page
    And I click on the Request Button
    And I click on the New Button
    And I enter details
    And I select Request Type
    Then I click on Create Button
    Then I Check the record saved in request list



  #  @Editor
    And I click on the Request Button
    And I click on unlock button
    Then I can edit record on Request List
#    And I enter edit abc
#    And I Click Back Button before save edit record
#    Then verify a pop up is generated with valid message

#  @Save
    And I click on the Request Button
    And I click on unlock button
    Then I can edit record on Request List
    And I click on save button

#  @Add
    And I click on the Request Button
    And I click on unlock button
    Then I can edit record on Request List
    Then I click on Add button
    And verify pop up is Display for requestor to add more TFNs
    Then I Click on Cancel Button

#  @AddNote
    And I click on the Request Button
    Then I can edit record on Request List
    Then I click on Add Note button
    Then I enter Note details
    Then I click on Add button and save it

#  @AutoAssign
    And I click on the Request Button
    And I click on unlock button
    Then I can edit record on Request List



# @AutoCustomTFN
    And I click on the Request Button
   And I click on unlock button
    Then I can edit record on Request List