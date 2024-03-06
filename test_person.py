import pytest
from person import Person
import os

# fixture


@pytest.fixture(params=['FirstName', 'OtherFirstName'])
def sample_person(request):
    return Person(request.param, 'LastName')


def test_repr(sample_person):
    assert str(sample_person) == 'FirstName LastName'


def test_initials(sample_person):
    assert sample_person.initials() == 'F L'


@pytest.fixture
def simple_tempfile():
    filename = '/tmp/abcd.txt'
    with open(filename) as f:
        f.write('abcd\n')
        f.write('efgh\n')
        f.write('ijkl\n')
        f.write('mnop\n')

    yield filename

    os.remove(filename)
