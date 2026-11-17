"""Tests for the load module"""
import pandas as pd

from life_expectancy.load import load_data

from . import FIXTURES_DIR


def test_load_data(eu_life_expectancy_raw):
    """Loading the raw fixture file returns its content as a DataFrame"""
    loaded = load_data(FIXTURES_DIR / "eu_life_expectancy_raw.tsv")
    pd.testing.assert_frame_equal(loaded, eu_life_expectancy_raw)
    assert not loaded.empty
