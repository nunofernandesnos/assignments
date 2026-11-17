"""Tests for the main module"""
from unittest.mock import patch

import pandas as pd

from life_expectancy import load
from life_expectancy.main import main


def test_main(eu_life_expectancy_raw, pt_life_expectancy_expected):
    """`main` returns the cleaned data and saves it without writing any file"""
    with patch("life_expectancy.load.load_data") as load_data_mock, patch(
        "pandas.DataFrame.to_csv"
    ) as to_csv_mock:
        load_data_mock.return_value = eu_life_expectancy_raw
        cleaned = main()
    load_data_mock.assert_called_once_with()
    to_csv_mock.assert_called_once_with(
        load.DATA_DIR / "pt_life_expectancy.csv", index=False
    )
    pd.testing.assert_frame_equal(
        cleaned.reset_index(drop=True), pt_life_expectancy_expected
    )


def test_main_other_region(eu_life_expectancy_raw):
    """`main` for another region saves to a region-specific file"""
    with patch("life_expectancy.load.load_data") as load_data_mock, patch(
        "pandas.DataFrame.to_csv"
    ) as to_csv_mock:
        load_data_mock.return_value = eu_life_expectancy_raw
        cleaned = main("FR")
    to_csv_mock.assert_called_once_with(
        load.DATA_DIR / "fr_life_expectancy.csv", index=False
    )
    assert set(cleaned["region"]) == {"FR"}
