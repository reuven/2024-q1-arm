import pytest
from person import Person

# fixture


@pytest.fixture
def sample_person():
    return Person('FirstName', 'LastName')


def test_repr(sample_person):
    assert str(p) == 'FirstName LastName'


def test_initials(sample_person):
    assert p.initials() == 'F L'
