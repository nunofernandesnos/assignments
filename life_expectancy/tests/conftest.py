"""Pytest configuration file"""
import pandas as pd
import pytest

from life_expectancy import load

from . import FIXTURES_DIR


@pytest.fixture(scope="session")
def eu_life_expectancy_raw() -> pd.DataFrame:
    """Fixture to load a sample of the raw input data"""
    return load.load_data(FIXTURES_DIR / "eu_life_expectancy_raw.tsv")


@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")
