import py
import pytest
from ArabicToRoman import IntegerToRoman
from ArabicToRoman import InputValidation

@pytest.mark.parametrize(
    "inputNumber, result",
    [
        (250, "CCL"),
        (2500, "MMD"),
        (1000000, "M̄")
    ]
)
def test_IntegerToRoman(inputNumber, result):
    assert IntegerToRoman(inputNumber) == result

@pytest.mark.parametrize(
    "InvInput, expected",
    [
        ("a", False),
        (-1, False)
    ]
)
def test_InputValidation(InvInput, expected):
    assert InputValidation(InvInput) == expected