from json import loads
import pytest
from behave import *
from django.contrib.auth.models import User, AnonymousUser
from mixer.backend.django import mixer

use_step_matcher("parse")

pytestmark = pytest.mark.django_db


@given("an instance of {model} with this attributes")
def step_impl(context, model):
    atts = loads(context.text)
    mixer.blend(model, **atts)


@step("set password {password} to the user {username}")
def step_impl(context, password, username):
    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()


@given("an authenticated user as the user {username}")
def step_impl(context, username):
    context.user = User.objects.filter(username=username).first()


@given("an anonymous user")
def step_impl(context):
    context.user = AnonymousUser()


@step("mock the method {method} with the response")
def step_impl(context, method):
    context.enable_mocking = True
    context.mocking_class_path = method
    context.mocking_response = loads(context.text)
