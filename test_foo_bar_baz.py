import pytest
import sys

from foo_bar_baz import foo_bar_baz

# Normal test cases
def test_basic():
    assert foo_bar_baz(2) == "1 2"
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(4) == "1 2 Foo 4"

    assert foo_bar_baz(6) == "1 2 Foo 4 Bar Foo"

    assert foo_bar_baz(9) == "1 2 Foo 4 Bar Foo 7 8 Foo"

    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

def test_existence():
    assert "Foo" in foo_bar_baz(10)
    assert "Baz" in foo_bar_baz(20)

    for i in range(4):
        assert "Bar" not in foo_bar_baz(i)

# @pytest.mark.parametrize("n, expected", [
#     (5, "1 2 Foo 4 Bar"),
#     (7, "1 2 Foo 4 Bar Foo 7"),
#     (10, "1 2 Foo 4 Bar Foo 7 8 Foo Bar"),
#     (12, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo"),
#     (14, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14"),
#     (18, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo"),
#     (19, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19"),
#     (20, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar"),
#     (21, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo"),
#     (22, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22"),
#     (23, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23"),
#     (24, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo"),
#     (25, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar"),
#     (26, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26"),
#     (27, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo"),
#     (28, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28"),
#     (29, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29"),
#     (30, "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz"),
# ])

# def test_lots(n, expected):
#     assert foo_bar_baz(n) == expected

# Edge test cases
def test_edge_cases():
    assert foo_bar_baz(-100) == ""
    assert foo_bar_baz(-1) == ""

    assert foo_bar_baz(0) == ""

    assert foo_bar_baz(1) == "1"

def test_incorrect():
    assert foo_bar_baz(10) != "1 2 3 4 5 6 7 8 9 10"

    assert foo_bar_baz(1) != 1

    assert foo_bar_baz(10) != 12345678910

    assert (foo_bar_baz(5) == "1 2 3 4 5") != True

# Correct Output Type
def test_output():
    assert isinstance(foo_bar_baz(0), str)
    assert isinstance(foo_bar_baz(10), str)
    assert isinstance(foo_bar_baz(100), str)
    assert isinstance(foo_bar_baz(-1), str)
    assert isinstance(foo_bar_baz(-10), str)

# Wrong Input Type
def test_wrong_input():
    with pytest.raises(TypeError):
        foo_bar_baz(9.5) 

    with pytest.raises(TypeError):
        foo_bar_baz(tuple) 

    with pytest.raises(TypeError):
        foo_bar_baz("Cheese") 

# Counts
def test_up_to_100():
    output = foo_bar_baz(100)
    assert output.count("Bar") == 14
    assert output.count("Baz") == 6

def test_up_to_20():
    output = foo_bar_baz(20)
    assert output.count("Baz") == 1
    assert output.count("Bar") == 3
    assert output.count("Foo") == 5

def test_neg_max_size():
    assert foo_bar_baz(-sys.maxsize) == "" # sadly max size is a little too big

# import pytest


# def test_basic_inputs():
#     from foo_bar_baz import foo_bar_baz

#     assert foo_bar_baz(0) == ""
#     assert foo_bar_baz(1) == "1"
#     assert foo_bar_baz(2) == "1 2"

#     assert foo_bar_baz(3) == "1 2 Foo"
#     assert foo_bar_baz(5) == "1 2 Foo 4 Bar"

#     assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

#     out = foo_bar_baz(30)
#     assert out.count("Foo") == 8
#     assert out.count("Bar") == 4
#     assert out.count("Baz") == 2

#     out = foo_bar_baz(100)
#     assert out.count("Foo") == 27
#     assert out.count("Bar") == 14
#     assert out.count("Baz") == 6

#     assert "Foo" in foo_bar_baz(333)
#     assert "Bar" in foo_bar_baz(200)

#     for i in range(15):
#         assert "Baz" not in foo_bar_baz(i)


# def test_output_type():
#     from foo_bar_baz import foo_bar_baz

#     assert isinstance(foo_bar_baz(0), str)
#     assert isinstance(foo_bar_baz(1), str)
#     assert isinstance(foo_bar_baz(10), str)
#     assert isinstance(foo_bar_baz(100), str)

#     assert isinstance(foo_bar_baz(-1), str)

#     assert isinstance(foo_bar_baz(3), str)
#     assert isinstance(foo_bar_baz(5), str)
#     assert isinstance(foo_bar_baz(30), str)


# def test_edge_case_ints():
#     from foo_bar_baz import foo_bar_baz

#     import sys
#     assert foo_bar_baz(-1) == ""
#     assert foo_bar_baz(-sys.maxsize) == ""


# def test_more_edge_case_ints():
#     from foo_bar_baz import foo_bar_baz

#     import sys
#     assert foo_bar_baz(-1) == ""
#     assert foo_bar_baz(-sys.maxsize) == ""

#     assert foo_bar_baz(-100) == ""
#     assert foo_bar_baz(0) == ""


# def test_wrong_type():
#     from foo_bar_baz import foo_bar_baz

#     with pytest.raises(TypeError):
#         foo_bar_baz("Rust")

#     with pytest.raises(TypeError):
#         foo_bar_baz(lambda x: x + 1)

#     with pytest.raises(TypeError):
#         foo_bar_baz(1.1)

#     with pytest.raises(TypeError):
#         foo_bar_baz(type)

#     with pytest.raises(TypeError):
#         foo_bar_baz(str)