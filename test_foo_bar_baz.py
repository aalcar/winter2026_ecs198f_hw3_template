import pytest

from foo_bar_baz import foo_bar_baz

# Normal test cases
def test_2():
    assert foo_bar_baz(2) == "1 2"

def test_3():
    assert foo_bar_baz(3) == "1 2 Foo"

def test_15():
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

@pytest.mark.parametrize("n, expected", [
    (5, "1 2 Foo 4 Bar"),
    (7, "1 2 Foo 4 Bar Foo 7"),
    (10, "1 2 Foo 4 Bar Foo 7 8 Foo Bar"),
    (12, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo"),
    (14, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14"),
    (18, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo"),
    (20, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar"),
    (21, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo"),
    (22, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22"),
])

def test_lots(n, expected):
    assert foo_bar_baz(n) == expected

# Edge test cases
def test_neg():
    assert foo_bar_baz(-100) == ""
    assert foo_bar_baz(-1) == ""

def test_0():
    assert foo_bar_baz(0) == ""

def test_1():
    assert foo_bar_baz(1) == "1"


# Incorrect implementation
def test_incorrect():
    assert foo_bar_baz(10) != "1 2 3 4 5 6 7 8 9 10"

# Incorrect test
def test_bad():
    assert (foo_bar_baz(5) == "1 2 3 4 5") != True