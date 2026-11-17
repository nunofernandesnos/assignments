"""Loading of the EU life expectancy data"""
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
INPUT_FILE = DATA_DIR / "eu_life_expectancy_raw.tsv"


def load_data(input_file: Path = INPUT_FILE) -> pd.DataFrame:
    """Load the raw TSV data."""
    return pd.read_csv(input_file, sep="\t")
