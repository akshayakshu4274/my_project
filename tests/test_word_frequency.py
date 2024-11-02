from ..word_frequency import word_frequency

def test_word_frequency():
    assert word_frequency("hello world hello") == [('hello', 2), ('world', 1)]

