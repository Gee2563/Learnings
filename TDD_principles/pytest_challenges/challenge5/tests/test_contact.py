from lib.contact import *
import pytest

@pytest.fixture
def create_contact():
    contact = Contact('George','07785366713')
    return contact

def test_contact_init(create_contact):
    #  test the attributes for contacts:

    # Test to ensure string length of name is qualified
    with pytest.raises(Exception) as err:
        contact = Contact('1','07785366713')
        contact1 = Contact(1, '07785366713')
    assert str(err.value) == 'Invalid input, name must be string and minimum 3 letters long'

    # Qualify number
    with pytest.raises(Exception) as err:
        contact = Contact('George', 1)
        contact1 = Contact('David', '124')
    assert str(err.value) == f'Invalid input, number must be string and 11 letters long'

    # test correct entry
    assert create_contact.name == 'George'
    assert create_contact.number == '07785366713'


def test_set_number(create_contact):
    # Test correct edit
    create_contact.set_number('07785366714')
    assert create_contact.number == '07785366714'


def test_format(create_contact):
    # test format of object
    assert create_contact.format() == 'George : 07785366713'

