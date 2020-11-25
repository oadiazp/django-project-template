from behave import register_type, use_fixture
from django.core.management import call_command

from bdd.fixtures import setup_wallets


def parse_int(string):
    return int(string)


register_type(int=parse_int)


def cast(string):
    try:
        return int(string)
    except ValueError:
        try:
            return float(string)
        except ValueError:
            return string


register_type(cast=cast)


def before_feature(context, feature):
    call_command('flush', verbosity=0, interactive=False)


fixture_registry = {
    'wallets': setup_wallets
}


def use_fixture_by_tag(tag, context, fixture_registry):
    _, fixture_name = tag.split('.')
    fixture_data = fixture_registry.get(fixture_name, None)
    if fixture_data is None:
        raise LookupError("Unknown fixture-tag: %s" % tag)

    fixture_func = fixture_data
    return use_fixture(fixture_func, context)


def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)
