import pytest
from person import Person

# fixture


def sample_person():
    return Person('FirstName', 'LastName')


def test_repr(sample_person):
    assert str(sample_person) == 'FirstName LastName'


def test_initials(sample_person):
    assert sample_person.initials() == 'F L'
