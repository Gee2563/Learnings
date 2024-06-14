import pytest
from lib.diary import *

text = 'Lorem ipsum dolor sit amet. Ut dolorem blanditiis ab consequatur deleniti sed dolores cupiditate! Eos autem molestias aut adipisci corrupti et voluptas omnis non ratione aliquam non repellat Quis ea autem dolor hic dolores expedita! Et sunt tempore non sunt quaerat ut officia labore qui quia numquam sit quaerat voluptate sed praesentium fugit est earum dolores. Aut autem quia ut mollitia voluptas et accusamus earum qui illum perspiciatis quo placeat odit. Aut earum quia et officia tempora id dolorem inventore qui unde similique? Vel cumque dolor ut aliquid libero est necessitatibus autem et ipsum similique et quas quae. Eum quasi tenetur ex molestiae maxime nam deleniti necessitatibus aut reiciendis enim sit magnam excepturi. Non repellendus veniam eos autem tempore est vitae perspiciatis ut odio porro quo sunt quia.'
title = 'My title'
diary_with_text_title = DiaryEntry(title, text)

def test_invalid_text_or_title():
    with pytest.raises(Exception) as err:
        DiaryEntry('','')
    assert str(err.value) == 'Please check the contents or title.'

def test_diary_format():
    result1 = diary_with_text_title.format()
    assert result1 == 'My title: Lorem ipsum dolor sit amet. Ut dolorem blanditiis ab consequatur deleniti sed dolores cupiditate! Eos autem molestias aut adipisci corrupti et voluptas omnis non ratione aliquam non repellat Quis ea autem dolor hic dolores expedita! Et sunt tempore non sunt quaerat ut officia labore qui quia numquam sit quaerat voluptate sed praesentium fugit est earum dolores. Aut autem quia ut mollitia voluptas et accusamus earum qui illum perspiciatis quo placeat odit. Aut earum quia et officia tempora id dolorem inventore qui unde similique? Vel cumque dolor ut aliquid libero est necessitatibus autem et ipsum similique et quas quae. Eum quasi tenetur ex molestiae maxime nam deleniti necessitatibus aut reiciendis enim sit magnam excepturi. Non repellendus veniam eos autem tempore est vitae perspiciatis ut odio porro quo sunt quia.'

def test_count_words():
    result2 = diary_with_text_title.count_words()
    assert result2 == 828

def test_count_wrong_input():
    with pytest.raises(Exception) as err:
        diary_with_text_title.reading_time('40')
    assert str(err.value) == 'Invalid input, input needs to be of type int.'

def test_reading_chunk() :   
    result4 = diary_with_text_title.reading_chunk(1,5)
    assert result4 == 'Lorem ipsum dolor sit amet.'

def test_reading_chunk_invalid_input():
    with pytest.raises(Exception) as err:
        diary_with_text_title.reading_chunk('1','5')
    assert str(err.value) == 'Please input an integer'
