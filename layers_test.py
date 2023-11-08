from typing import get_type_hints

import pytest

from layers import create_layers


@pytest.mark.parametrize(
    "layers,expected_output",
    [
        (1, "A"),
        (2, "BBB\nBAB\nBBB"),
        (3, "CCCCC\nCBBBC\nCBABC\nCBBBC\nCCCCC"),
        (4, "DDDDDDD\nDCCCCCD\nDCBBBCD\nDCBABCD\nDCBBBCD\nDCCCCCD\nDDDDDDD"),
    ],
)
def test_create_layers(layers, expected_output):
    assert create_layers(layers) == expected_output


# Test to check function argument type
def test_argument_type():
    hints = get_type_hints(create_layers)
    assert hints["layers"] == int, "Argument type must be int"


# Test to check function return type
def test_return_type():
    hints = get_type_hints(create_layers)
    assert hints["return"] == str, "Return type must be str"
