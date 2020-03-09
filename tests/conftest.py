import pytest
from email.utils import formatdate


@pytest.fixture
def request_date():
    return formatdate(timeval=None, localtime=False, usegmt=True)


@pytest.fixture
def api_secret_key():
    return "secret_key"
