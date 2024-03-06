import pytest
from person import Person

p = Person('FirstName', 'LastName')


def test_repr():
    assert str(p) == 'FirstName LastName'


def test_initials():
    assert p.initials() == 'F L'
