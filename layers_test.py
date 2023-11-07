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
