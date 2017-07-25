from behave import *
import os, sys
from hamcrest import *

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from models import users


@when('we GET the list of users at endpoint "{req}"')
def step_impl(context, req):
    context.response = users.get_list_user(req)


@then('we receive a list JSON object contains {number:d} users')
def step_impl(context, number):
    qty_users = len(context.response.json())
    users.verify_successful_response(context.response)
    assert_that(qty_users, equal_to(number))


@given('we GET a user with {username} at endpoint "{req}"')
@when('we GET a user with {username} at endpoint "{req}"')
def step_impl(context, username, req):
    context.response = users.search_with_username(req, username)


@step("the user information in JSON object must have {name},{email},{website}")
def step_impl(context, name, email, website):
    users.verify_successful_response(context.response)
    users.verify_user_information_match(context.response.json()[0], name, email, website)


@given("there is an user information")
def step_impl(context):
    user_information = {}
    for row in context.table:
        user_information['username'] = row['username']
        user_information['name'] = row['name']
        user_information['email'] = row['email']
        user_information['website'] = row['website']
    context.user_info = user_information


@when('we POST the user information at endpoint "{req}"')
def step_impl(context, req):
    context.response = users.create_new_user(req, context.user_info)


@then("the new user must be created successfully")
def step_impl(context):
    users.verify_successful_response(context.response)


@given('we want to update the user "{user_name}" with following information')
def step_impl(context, user_name):
    user_information = {}
    for row in context.table:
        user_information['username'] = user_name
        user_information['name'] = row['name']
        user_information['email'] = row['email']
        user_information['website'] = row['website']
    context.user_info = user_information


@when('we PUT the user update information at endpoint "{req}"')
def step_impl(context, req):
    user_name = context.user_info['username']
    del context.user_info['username']
    user_id = users.search_with_username("/users?username=", user_name).json()[0]['id']
    context.response = users.update_user(req, str(user_id), context.user_info)


@then("the user must be updated successfully")
def step_impl(context):
    users.verify_successful_response(context.response)


@when('we DELETE the user at endpoint "{req}"')
def step_impl(context, req):
    user_id = context.response.json()[0]['id']
    context.response = users.delete_user_with_id(req, str(user_id))


@then("the user must be deleted successfully")
def step_impl(context):
    users.verify_successful_response(context.response)


@then("the response must not contains any user result")
def step_impl(context):
    users.verify_successful_response(context.response)
    users.verify_user_search_result_is_empty(context.response.text)