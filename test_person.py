import pytest
from person import Person

# fixture


@pytest.fixture(params=['FirstName', 'OtherFirstName'])
def sample_person(request):
    return Person(request.param, 'LastName')


def test_repr(sample_person):
    assert str(sample_person) == 'FirstName LastName'


def test_initials(sample_person):
    assert sample_person.initials() == 'F L'
