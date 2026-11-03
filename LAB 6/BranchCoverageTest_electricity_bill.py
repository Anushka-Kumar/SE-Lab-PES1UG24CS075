import pytest
from electricity_bill import energy_charge, late_fee, subsidy


# ENERGY CHARGE - BRANCH TESTS

def test_invalid_connection():
    with pytest.raises(ValueError, match="unknown connection"):
        energy_charge(100, "industrial")


def test_valid_domestic_connection():
    assert energy_charge(50, "domestic") == 200


def test_negative_units():
    with pytest.raises(ValueError, match="invalid units"):
        energy_charge(-10, "domestic")


def test_non_negative_units():
    assert energy_charge(0, "domestic") == 50


def test_units_at_lower_boundary():
    assert energy_charge(100, "domestic") == 350


def test_units_between_100_and_300():
    assert energy_charge(200, "domestic") == 850


def test_units_at_upper_boundary():
    assert energy_charge(300, "domestic") == 1350


def test_units_above_300():
    assert energy_charge(301, "domestic") == 1358


def test_commercial_connection():
    assert energy_charge(50, "commercial") == 450


# LATE FEE - BRANCH TESTS

def test_days_late_zero():
    assert late_fee(500, 0) == 0


def test_days_late_negative():
    assert late_fee(500, -5) == 0


def test_days_late_within_15():
    assert late_fee(500, 10) == 50


def test_days_late_exactly_15():
    assert late_fee(500, 15) == 50


def test_days_late_above_15():
    assert late_fee(500, 16) == 100


def test_bill_amount_below_2000():
    assert late_fee(1500, 16) == 100


def test_bill_amount_exactly_2000():
    assert late_fee(2000, 16) == 100


def test_bill_amount_above_2000():
    assert late_fee(2500, 16) == 225


# SUBSIDY - BRANCH TESTS

def test_senior_at_100_units():
    assert subsidy(100, True, False) == 50


def test_non_senior_at_100_units():
    assert subsidy(100, False, False) == 0


def test_senior_above_100_units():
    assert subsidy(101, True, False) == 0


def test_senior_below_100_units():
    assert subsidy(50, True, False) == 50


def test_solar_available():
    assert subsidy(200, False, True) == 100


def test_solar_not_available():
    assert subsidy(200, False, False) == 0


def test_solar_at_300_units():
    assert subsidy(300, False, True) == 100


def test_solar_above_300_units():
    assert subsidy(301, False, True) == 0


def test_senior_and_solar():
    assert subsidy(100, True, True) == 150


def test_senior_and_solar_above_300():
    assert subsidy(301, True, True) == 0