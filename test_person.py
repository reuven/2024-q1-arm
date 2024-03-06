import pytest
from person import Person

# fixture


@pytest.fixture
def sample_person():
    return Person('FirstName', 'LastName')


def test_repr(sample_person):
    assert str(sample_person) == 'FirstName LastName'


def test_initials(sample_person):
    assert sample_person.initials() == 'F L'


def test_initials_are(sample_person):
    assert sample_person.initials_are('F L')
