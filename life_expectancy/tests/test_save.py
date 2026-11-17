"""Tests for the save module"""
from pathlib import Path
from unittest.mock import patch

from life_expectancy.save import save_data


def test_save_data(pt_life_expectancy_expected):
    """Saving data calls `to_csv` without writing any file"""
    output_file = Path("out.csv")
    with patch("pandas.DataFrame.to_csv") as to_csv_mock:
        save_data(pt_life_expectancy_expected, output_file)
    to_csv_mock.assert_called_once_with(output_file, index=False)
