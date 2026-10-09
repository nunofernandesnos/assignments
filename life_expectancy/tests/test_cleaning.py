"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy import cleaning
from life_expectancy.cleaning import clean_data
from . import OUTPUT_DIR


def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    clean_data()
    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )


def test_clean_data_other_region(tmp_path, monkeypatch):
    """Run `clean_data` for a non-default region and check the output file"""
    monkeypatch.setattr(cleaning, "DATA_DIR", tmp_path)
    clean_data("FR")
    fr_life_expectancy = pd.read_csv(tmp_path / "fr_life_expectancy.csv")
    assert not fr_life_expectancy.empty
    assert set(fr_life_expectancy["region"]) == {"FR"}
