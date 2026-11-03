import pytest
from electricity_bill import energy_charge, late_fee, subsidy


# ENERGY CHARGE TEST CASES

def test_domestic_low_usage():
    assert energy_charge(50, "domestic") == 200


def test_commercial_low_usage():
    assert energy_charge(50, "commercial") == 450


def test_energy_charge_exactly_100_units():
    assert energy_charge(100, "domestic") == 350


def test_energy_charge_above_100_units():
    assert energy_charge(101, "domestic") == 355


def test_energy_charge_exactly_300_units():
    assert energy_charge(300, "domestic") == 1350


def test_energy_charge_above_300_units():
    assert energy_charge(301, "domestic") == 1358


def test_energy_charge_zero_units():
    assert energy_charge(0, "domestic") == 50


def test_energy_charge_invalid_connection():
    with pytest.raises(ValueError, match="unknown connection"):
        energy_charge(100, "industrial")


def test_energy_charge_negative_units():
    with pytest.raises(ValueError, match="invalid units"):
        energy_charge(-10, "domestic")


# LATE FEE TEST CASES

def test_late_fee_zero_days():
    assert late_fee(500, 0) == 0


def test_late_fee_negative_days():
    assert late_fee(500, -5) == 0


def test_late_fee_one_day():
    assert late_fee(500, 1) == 50


def test_late_fee_exactly_15_days():
    assert late_fee(500, 15) == 50


def test_late_fee_more_than_15_days():
    assert late_fee(500, 16) == 100


def test_late_fee_bill_exactly_2000():
    assert late_fee(2000, 16) == 100


def test_late_fee_bill_above_2000():
    assert late_fee(2500, 16) == 225


# SUBSIDY TEST CASES

def test_senior_citizen_subsidy():
    assert subsidy(100, True, False) == 50


def test_non_senior_citizen():
    assert subsidy(100, False, False) == 0


def test_senior_citizen_above_100_units():
    assert subsidy(150, True, False) == 0


def test_solar_subsidy():
    assert subsidy(200, False, True) == 100


def test_senior_with_solar_subsidy():
    assert subsidy(100, True, True) == 150


def test_solar_subsidy_above_300_units():
    assert subsidy(301, False, True) == 0


def test_senior_with_solar_above_300_units():
    assert subsidy(301, True, True) == 0


def test_no_subsidy():
    assert subsidy(200, False, False) == 0