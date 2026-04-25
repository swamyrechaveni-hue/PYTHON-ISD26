import pytest
from src.temperature_converter_function import convert


@pytest.mark.parametrize(
    "scale, temp, expected_c, expected_f, expected_k",
    [
        ("C", "0", 0.0, 32.0, 273.15),
        ("F", "32", 0.0, 32.0, 273.15),
        ("K", "273.15", 0.0, 32.0, 273.15),
        ("Z", "273.15", 0.0, 32.0, 273.15),
    ],
)
def test_temperature_converter(scale, temp, expected_c, expected_f, expected_k):
    c, f, k = convert(scale, temp)

    assert c == pytest.approx(expected_c, abs=0.01)
    assert f == pytest.approx(expected_f, abs=0.01)
    assert k == pytest.approx(expected_k, abs=0.01)