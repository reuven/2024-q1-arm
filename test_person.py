import pytest
from person import Person


def test_repr():
    p = Person('FirstName', 'LastName')
    assert str(p) == 'FirstName LastName'


def test_initials():
    p = Person('FirstName', 'LastName')
    assert p.initials() == 'F L'
