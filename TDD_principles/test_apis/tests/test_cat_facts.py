from lib.cat_facts import CatFacts
from unittest.mock import Mock

def test_cat_provide():
    request = Mock()
    response = Mock()
    request.get.return_value = response
    response.json.return_value = {
        'fact': "A cat's smell is their strongest sense, and they rely on this leading sense to identify people and objects; a feline's sense of smell is 14x better than a human's."
    }

    cat_fact = CatFacts(request)
    assert cat_fact.provide() == "Cat fact: A cat's smell is their strongest sense, and they rely on this leading sense to identify people and objects; a feline's sense of smell is 14x better than a human's."