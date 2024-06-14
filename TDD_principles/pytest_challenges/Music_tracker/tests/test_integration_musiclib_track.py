from lib.music_library import *
from lib.track import *
from unittest.mock import Mock
import pytest


def test_count_mocklibrary():
    fake_library = MusicLibrary()
    fake_track1 = Mock()
    fake_track1.title = 'Title1'
    fake_track1.artist = 'Artist1'

    fake_track2 = Mock()
    fake_track2.title = 'Title2'
    fake_track2.artist = 'Artist2'

    fake_library.add(fake_track1)
    fake_library.add(fake_track2)


    assert len(fake_library.list) == 2

def test_search_mock_library():
    fake_library = MusicLibrary()
    fake_track1 = Mock()
    fake_track1.title = 'Title1'
    fake_track1.artist = 'Artist1'

    fake_track2 = Mock()
    fake_track2.title = 'Title2'
    fake_track2.artist = 'Artist2'

    fake_library.add(fake_track1)
    fake_library.add(fake_track2)


    assert fake_library.search('Tit') == [fake_track1, fake_track2]

def test_loop():
    while True:
        fake_library = MusicLibrary()
        fake_track1 = Mock()
        fake_track1.title = 'Title1'
        fake_track1.artist = 'Artist1'

        fake_track2 = Mock()
        fake_track2.title = 'Title2'
        fake_track2.artist = 'Artist2'

        fake_library.add(fake_track1)
        fake_library.add(fake_track2)


        assert fake_library.search('Tit') == [fake_track1, fake_track2]