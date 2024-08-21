from behave import fixture, use_fixture
from support.config import API_BASE_URL


@fixture
def init_context(context):
    context.base_url = API_BASE_URL
    context.headers = {
        "Content-Type": "application/json"
    }
    yield context


def before_all(context):
    use_fixture(init_context, context)
