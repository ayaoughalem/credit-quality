
import pytest

from credit import calculate_risk


def test_low_risk():
    assert calculate_risk(10000, 2000, 25) == "LOW"


def test_medium_risk():
    assert calculate_risk(10000, 4000, 25) == "MEDIUM"


def test_high_risk():
    assert calculate_risk(10000, 7000, 25) == "HIGH"


def test_boundary_low_medium():
    assert calculate_risk(10000, 3000, 25) == "LOW"


def test_boundary_medium_high():
    assert calculate_risk(10000, 6000, 25) == "MEDIUM"


def test_zero_income():
    with pytest.raises(ValueError):
        calculate_risk(0, 1000, 25)


def test_negative_income():
    with pytest.raises(ValueError):
        calculate_risk(-1000, 100, 25)


def test_negative_debt():
    with pytest.raises(ValueError):
        calculate_risk(10000, -100, 25)


def test_underage():
    with pytest.raises(ValueError):
        calculate_risk(10000, 1000, 17)
