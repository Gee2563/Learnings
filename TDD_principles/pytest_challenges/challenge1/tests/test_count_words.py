from lib.count_words import *

def test_count_words():
    result = count_words('This sentence has 5 words.')
    assert result == 5
