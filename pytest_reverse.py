import reverses


def test_empty():
    test_case = ""
    answer = reverses.reverse(test_case)
    assert answer == ""


def test_single():
    test_case = "abc"
    answer = reverses.reverse(test_case)
    assert answer == "abc"

def test_two_words():
    test_case = "Hello World"
    answer = reverses.reverse(test_case)
    assert answer == "World Hello"

def test_sentence():
    test_case = "My name is V Tadimeti"
    answer = reverses.reverse(test_case)
    assert answer == "Tadimeti V is name My"