import pytest
from person import Person

# fixture


@pytest.fixture
def sample_person():
    return Person('FirstName', 'LastName')


def test_repr():
    p = Person('FirstName', 'LastName')
    assert str(p) == 'FirstName LastName'


def test_initials():
    p = Person('FirstName', 'LastName')
    assert p.initials() == 'F L'
