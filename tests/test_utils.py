from jformat.utils import formatter
import pytest


def test_typeerror():
    with pytest.raises(TypeError):
        formatter([])

def test_string_is_sorted():
    json_string = '{"name": "John", "last_name": "Smith"}'
    result = formatter(json_string)
    expected = """{
    "last_name": "Smith",
    "name": "John"
}"""
    assert result == expected