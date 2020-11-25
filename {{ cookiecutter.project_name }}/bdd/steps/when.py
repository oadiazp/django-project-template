import json
from unittest.mock import patch

from behave import when, use_step_matcher
from django.test import RequestFactory

from apps.core.schema import schema

use_step_matcher('parse')


@when("a {method} request to {url} is made with the body")
def step_impl(context, method, url):
    client = context.test.client
    method_fn = getattr(client, method.lower())
    context.response = method_fn(
        url,
        data=context.text,
        content_type='application/json'
    )
    context.body = json.loads(
        context.response.render().content
    )


@when("I send a GraphQL request with the body")
def step_impl(context):
    request_factory = RequestFactory()
    request = request_factory.post('/graphql/')
    request.user = context.user

    if not hasattr(context, 'enable_mocking') or not context.enable_mocking:
        context.response = schema.execute(
            context.text,
            context=request
        )
    else:
        with patch(context.mocking_class_path) as mock:
            mock.return_value = context.mocking_response
            context.response = schema.execute(
                context.text,
                context=request
            )

    context.body = context.response.to_dict()
