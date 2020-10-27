from xmljson import parker, Parker
from xml.etree.ElementTree import fromstring, ParseError
from json import dumps
import pytest
import sys

def test_single_empty():
    # arrange
    input = open("./test-data/test_input/single_empty.xml", "r")
    input_text = input.read()
    print("input_text: " + input_text)

    expected = open("./test-data/expected_output/single_empty.json", "r")
    expected_text = expected.read()
    print("expected_text: " + expected_text)

    # act
    res = dumps(parker.data(fromstring(input_text), preserve_root=True))
    print("res: " + str(res))

    # assert
    assert res == expected_text

def test_single_single():
    # arrange
    input = open("./test-data/test_input/single_single.xml", "r")
    input_text = input.read()
    print("input_text: " + input_text)

    expected = open("./test-data/expected_output/single_single.json", "r")
    expected_text = expected.read()
    print("expected_text: " + expected_text)

    # act
    res = dumps(parker.data(fromstring(input_text), preserve_root=True))
    print("res: " + str(res))

    # assert
    assert res == expected_text

def test_multiple_empty():
    # arrange
    input = open("./test-data/test_input/multiple_empty.xml", "r")
    input_text = input.read()
    print("input_text: " + input_text)

    expected = open("./test-data/expected_output/multiple_empty.json", "r")
    expected_text = expected.read()
    print("expected_text: " + expected_text)

    # act
    res = dumps(parker.data(fromstring(input_text), preserve_root=True))
    print("res: " + str(res))

    # assert
    assert res == expected_text

def test_multiple_single():
    # arrange
    input = open("./test-data/test_input/multiple_single.xml", "r")
    input_text = input.read()
    print("input_text: " + input_text)

    expected = open("./test-data/expected_output/multiple_single.json", "r")
    expected_text = expected.read()
    print("expected_text: " + expected_text)

    # act
    res = dumps(parker.data(fromstring(input_text), preserve_root=True))
    print("res: " + str(res))

    # assert
    assert res == expected_text

def test_multiple_multiple():
    # arrange
    input = open("./test-data/test_input/multiple_multiple.xml", "r")
    input_text = input.read()
    print("input_text: " + input_text)

    expected = open("./test-data/expected_output/multiple_multiple.json", "r")
    expected_text = expected.read()
    print("expected_text: " + expected_text)

    # act
    res = dumps(parker.data(fromstring(input_text), preserve_root=True))
    print("res: " + str(res))

    # assert
    assert res == expected_text

def test_nested_empty():
    # arrange
    input = open("./test-data/test_input/nested_empty.xml", "r")
    input_text = input.read()
    print("input_text: " + input_text)

    expected = open("./test-data/expected_output/nested_empty.json", "r")
    expected_text = expected.read()
    print("expected_text: " + expected_text)

    # act
    res = dumps(parker.data(fromstring(input_text), preserve_root=True))
    print("res: " + str(res))

    # assert
    assert res == expected_text

def test_nested_single():
    # arrange
    input = open("./test-data/test_input/nested_single.xml", "r")
    input_text = input.read()
    print("input_text: " + input_text)

    expected = open("./test-data/expected_output/nested_single.json", "r")
    expected_text = expected.read()
    print("expected_text: " + expected_text)

    # act
    res = dumps(parker.data(fromstring(input_text), preserve_root=True))
    print("res: " + str(res))

    # assert
    assert res == expected_text

def test_nested_multiple():
    # arrange
    input = open("./test-data/test_input/nested_multiple.xml", "r")
    input_text = input.read()
    print("input_text: " + input_text)

    expected = open("./test-data/expected_output/nested_multiple.json", "r")
    expected_text = expected.read()
    print("expected_text: " + expected_text)

    # act
    res = dumps(parker.data(fromstring(input_text), preserve_root=True))
    print("res: " + str(res))

    # assert
    assert res == expected_text

def test_invalid_input_path():
    # arrange & assert
    with pytest.raises(FileNotFoundError):
        input = open("./test-data/test_input/this_is_not_a_file.xml", "r")
        input_text = input.read()
        print("input_text: " + input_text)

def test_invalid_xml():
    # arrange
    input = open("./test-data/test_input/invalid.xml", "r")
    input_text = input.read()
    print("input_text: " + input_text)
    
    # act & assert
    with pytest.raises(ParseError, match=r".*syntax error.*"):
        json_str = dumps(parker.data(fromstring(input_text), preserve_root=False))

def test_empty():
    # arrange
    file = open("./test-data/test_input/empty.xml", "r")
    file_text = file.read()

    # act & assert
    with pytest.raises(ParseError, match=r".*no element found.*"):
        json_str = dumps(parker.data(fromstring(file_text)), preserve_root=True)

if __name__ == '__main__':
    globals()[sys.argv[1]]()