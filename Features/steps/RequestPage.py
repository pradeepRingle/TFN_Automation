import time

from behave import then
from Locators import RequestPage


@then(u"I am on the home page")
def steps_impl(context):
    print(context.lib.get_title())


@then(u"I click on the Request Button")
def steps_impl(context):
    context.lib.double_click_using_action_chains(RequestPage.reqText1)


@then(u"I click on the New Button")
def steps_impl(context):
    context.lib.click_event(RequestPage.reqButton1)


@then(u"I enter details")
def steps_impl(context):
    context.reqTitle1 = context.RandomString
    context.lib.send_keyboard_keys(RequestPage.reqTitle1, context.reqTitle1)
    context.lib.send_keyboard_keys(RequestPage.reqNumberTFN, 1)


@then(u"I select Request Type")
def steps_impl(context):
    context.lib.click_event(RequestPage.reqType)


@then(u"I click on Create Button")
def steps_impl(context):
    context.lib.click_event(RequestPage.reqCreate)


@then(u"I Check the record saved in request list")
def steps_impl(context):
    data = context.lib.get_text(RequestPage.reqRecord)
    assert data == context.reqTitle1


@then(u'I can edit record on Request List')
def steps_impl(context):
    time.sleep(5)
    context.lib.click_event(RequestPage.reqEdit)


@then(u'I click on unlock button')
def steps_impl(context):
    time.sleep(5)
    context.lib.click_event(RequestPage.reqUnlock)


@then(u'I enter edit {abc}')
def steps_impl(context, abc):
    context.lib.click_event(RequestPage.reqText2)
    context.lib.send_keyboard_edit_keys(RequestPage.reqText2, abc)


@then(u'I Click Back Button before save edit record')
def steps_impl(context):
    context.lib.click_event(RequestPage.reqBack)


@then(u'verify a pop up is generated with valid message')
def step_impl(context):
    context.lib.verify_mandatory_message(RequestPage.reqPopUpMessage)


@then(u'I Click on Cancel Button')
def steps_impl(context):
    context.lib.click_event(RequestPage.reqCancel)


@then(u'I click on save button')
def steps_impl(context):
    context.lib.click_event(RequestPage.reqSave)


@then(u"I click on Add button")
def steps_impl(context):
    time.sleep(15)
    context.lib.single_click_using_action_chains(RequestPage.reqAddButton)


@then(u'verify pop up is Display for requestor to add more TFNs')
def step_impl(context):
    time.sleep(5)
    context.lib.verify_pop_up_message(RequestPage.reqPopUpMessage2)


@then(u"I click on Delete button")
def steps_impl(context):
    context.lib.click_event(RequestPage.reqAddButton)


@then(u"I click on Add Note button")
def steps_impl(context):
    time.sleep(15)
    context.lib.click_event(RequestPage.reqAddNoteButton)


@then(u"I enter Note details")
def steps_impl(context):
    time.sleep(5)
    context.reqText3 = context.RandomString
    context.lib.send_keyboard_keys(RequestPage.reqText3, context.reqText3)


@then(u"I click on Add button and save it")
def steps_impl(context):
    context.lib.click_event(RequestPage.reqAddButton2)


@then(u'I click to data')
def steps_impl(context):
    context.lib.click_event(RequestPage.reqData)
