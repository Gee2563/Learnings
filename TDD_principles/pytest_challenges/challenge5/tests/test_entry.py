import pytest
from lib.entry import *

@pytest.fixture
def create_entry():
    entry = Entry('Today I swam the dolphin')
    entry.set_reading_time(5)
    return entry

def test_init(create_entry):
    assert create_entry.text == 'Today I swam the dolphin'

    with pytest.raises(Exception) as err:
        entry = Entry(1)
        entry = Entry('1')
    assert str(err.value) == 'Invalid input'

def test_set_reading_time(create_entry):
    assert create_entry.reading_time == 1
    with pytest.raises(Exception) as err:
        entry = Entry('I walked the dog today.')
        entry.set_reading_time('a')
    assert str(err.value) == 'Invalid wpm'


def test_check_and_return_contacts():
    # Checks with . at the end (and other specials)
    entry = Entry('Dear diary, #Yen lost her phone. her new number is 07785577613.')
    # hashtag will be used in entries to signal an element to store
    assert entry.check_and_return_contact_info() == {
        'Yen' : "+447785577613"
    }
    # Checks for identical numbers, if name is the same and number is different, save name as name-1
    
    with pytest.raises(Exception) as er:
        entry = Entry('Dear diary, #Yen lost her phone. her new number is 07785577613.Dear diary, #George lost her phone. her new number is 07785577613.')
    assert str(er.value) == 'Too many names.'
    entry = Entry('Dear diary, #Yen lost her phone. her new number is 07785577613.Dear diary, #Yen lost her phone. her new number is 07785577613.')
    assert entry.check_and_return_contact_info() == { 'Yen':'+447785577613' }
    
    # Checks for more complex sentences -> 1st #Person1 , 2nd #Person2, raise exception if 2 names, 1 number , if 1 person, 2 nums -> save as name1,num1, name2, num2
    entry = Entry('Dear diary, #Yen and #David both lost their phones. Their new numbers are +447785577613 and 07785575613')
    assert entry.check_and_return_contact_info() == {
        'Yen': '+447785577613',
        'David': '+447785575613'
    }
    entry = Entry('Dear diary, #Yen lost her phones. Her new numbers are 07785577613 and 07785575613')
    assert entry.check_and_return_contact_info == {
        'Yen' : '+447785577613',
        'Additional' : ['+447785575613']
    }

