from xmljson import parker, Parker
from xml.etree.ElementTree import fromstring, ParseError
from json import dumps
import pytest
import sys

def invalid():
    assert True

def test_empty():
    # arrange
    file = open("./test-data/test_input/empty.xml", "r")
    file_text = file.read()

    # act & assert
    with pytest.raises(ParseError, match=r".*no element found.*"):
        json_str = dumps(parker.data(fromstring(file_text)), preserve_root=True)

def test_no_children():
    # arrange
    input = open("./test-data/test_input/no_children.xml", "r")
    input_text = input.read()
    print("input_text: " + input_text)

    expected = open("./test-data/expected_output/no_children.json", "r")
    expected_text = expected.read()
    print("expected_text: " + expected_text)

    # act
    res = dumps(parker.data(fromstring(input_text), preserve_root=True))
    print("res: " + str(res))

    # assert
    assert res == expected_text
    

def test_single_children():
    # arrange
    input = open("./test-data/test_input/single_child.xml", "r")
    input_text = input.read()
    print("input_text: " + input_text)

    expected = open("./test-data/expected_output/single_child.json", "r")
    expected_text = expected.read()
    print("expected_text: " + expected_text)

    # act
    res = dumps(parker.data(fromstring(input_text), preserve_root=True))
    print("res: " + str(res))

    # assert
    assert res == expected_text

def test_multiple_children_same_name():
    # arrange
    input = open("./test-data/test_input/multiple_children_same_name.xml", "r")
    input_text = input.read()
    print("input_text: " + input_text)

    expected = open("./test-data/expected_output/multiple_children_same_name.json", "r")
    expected_text = expected.read()
    print("expected_text: " + expected_text)

    # act
    res = dumps(parker.data(fromstring(input_text), preserve_root=True))
    print("res: " + str(res))

    # assert
    assert res == expected_text

def test_multiple_children_different_name():
    # arrange
    input = open("./test-data/test_input/multiple_children_different_name.xml", "r")
    input_text = input.read()
    print("input_text: " + input_text)

    expected = open("./test-data/expected_output/multiple_children_different_name.json", "r")
    expected_text = expected.read()
    print("expected_text: " + expected_text)

    # act
    res = dumps(parker.data(fromstring(input_text), preserve_root=True))
    print("res: " + str(res))

    # assert
    assert res == expected_text

def test_nested():
    # arrange
    input = open("./test-data/test_input/nested.xml", "r")
    input_text = input.read()
    print("input_text: " + input_text)

    expected = open("./test-data/expected_output/nested.json", "r")
    expected_text = expected.read()
    print("expected_text: " + expected_text)

    # act
    res = dumps(parker.data(fromstring(input_text), preserve_root=True))
    print("res: " + str(res))

    # assert
    assert res == expected_text

if __name__ == '__main__':
    globals()[sys.argv[1]]()