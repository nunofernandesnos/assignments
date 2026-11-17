"""Tests for the clean module"""
import pandas as pd

from life_expectancy.clean import clean_data


def test_clean_data(eu_life_expectancy_raw, pt_life_expectancy_expected):
    """Cleaning the raw sample for the default region gives the expected output"""
    cleaned = clean_data(eu_life_expectancy_raw)
    pd.testing.assert_frame_equal(
        cleaned.reset_index(drop=True), pt_life_expectancy_expected
    )


def test_clean_data_other_region(eu_life_expectancy_raw):
    """Cleaning for another region only keeps that region"""
    cleaned = clean_data(eu_life_expectancy_raw, "FR")
    assert not cleaned.empty
    assert set(cleaned["region"]) == {"FR"}


def test_clean_data_does_not_modify_input(eu_life_expectancy_raw):
    """Cleaning must not mutate the raw DataFrame"""
    before = eu_life_expectancy_raw.copy()
    clean_data(eu_life_expectancy_raw)
    pd.testing.assert_frame_equal(eu_life_expectancy_raw, before)
