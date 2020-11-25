from json import loads

from behave import *
from django.http import HttpResponse
from jsonpath_ng import parse
from pytest import fail

from apps.core import models

use_step_matcher("parse")


@then("the REST response is successful")
def step_impl(context):
    status_code = context.response.status_code
    assert 200 <= status_code < 299, f'Received status: {status_code}'


@step("the amount of records on {model} is {amount:int}")
def step_impl(context, model, amount):
    model_class = getattr(models, model)
    result = model_class.objects.count()

    assert result == amount, f'Received amount: {result}'


@step("I have an {model} with this attributes")
def step_impl(context, model):
    filters = loads(context.text)

    model_class = getattr(models, model)
    assert model_class.objects.filter(**filters).exists()


@step("{value:cast} is in the path {path}")
def step_impl(context, value, path):
    expresion = parse(path)

    if not hasattr(context, 'body'):
        if isinstance(context.response, HttpResponse):
            context.body = loads(context.response.render().content)

        context.body = {
            'data': context.response.data
        }

    result = expresion.find(context.body)

    if not isinstance(result, list) or len(result) == 0:
        fail(f"""
Expected value: {value}
Actual value: {result}
Response: {context.body}
        """)

    result = result[0].value
    assert result == value, f"""
Expected value: {value}
Actual value: {result}
Response: {context.body}
    """


@step("{path} is not empty")
def step_impl(context, path):
    expresion = parse(path)

    if not hasattr(context, 'body'):
        context.body = loads(context.response.render().content)

    result = expresion.find(context.body)[0].value

    assert result is not None, f'Path: {result}'


@then("the response is a bad requested")
def step_impl(context):
    status_code = context.response.status_code

    assert 400 <= status_code < 499, f'Status code: {status_code}'


@then("the mutation response is successful")
def step_impl(context):
    print(context.body)

    data = context.body['data']
    first_key = list(data.keys())[0]

    assert data[first_key]['ok']


@then("the response is successful")
def step_impl(context):
    assert 'data' in context.body.keys(), f'Response: {context.body}'


@then("the mutation response is wrong")
def step_impl(context):
    print(context.body)

    data = context.body['data']
    first_key = list(data.keys())[0]

    assert not data[first_key]['ok']


@step("there is {amount:cast} items in the path {path}")
def step_impl(context, amount, path):
    expresion = parse(path)
    result = expresion.find(context.body)

    assert len(result) == amount, f"""
Actual amount: {len(result)}
Expected amount: {amount}, 
    """
