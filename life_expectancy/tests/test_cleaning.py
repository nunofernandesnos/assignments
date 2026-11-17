"""Tests for the cleaning module"""
from pathlib import Path
from unittest.mock import patch

import pandas as pd

from life_expectancy.cleaning import clean_data, load_data, save_data

from . import FIXTURES_DIR


def test_load_data(eu_life_expectancy_raw):
    """Loading the raw fixture file returns its content as a DataFrame"""
    loaded = load_data(FIXTURES_DIR / "eu_life_expectancy_raw.tsv")
    pd.testing.assert_frame_equal(loaded, eu_life_expectancy_raw)
    assert not loaded.empty


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


def test_save_data(pt_life_expectancy_expected):
    """Saving data calls `to_csv` without writing any file"""
    output_file = Path("out.csv")
    with patch("pandas.DataFrame.to_csv") as to_csv_mock:
        save_data(pt_life_expectancy_expected, output_file)
    to_csv_mock.assert_called_once_with(output_file, index=False)
