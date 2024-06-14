from lib.track import *
import pytest


def test_track_init():
    track = Track('Title1', 'Artist1')
    assert track.title == 'Title1'
    assert track.artist == 'Artist1'
    with pytest.raises(Exception) as err:
        track1 = Track(1, 'Artist')
        track2 = Track('1',1)
    assert str(err.value ) == 'Invalid input'


def test_matches():
    track = Track('Title1','Artist1')
    assert track.matches('Tit') == True
    with pytest.raises(Exception) as err:
        Track('Title1', 'Artist1').matches(1)
    assert str(err.value) == 'Invalid input'