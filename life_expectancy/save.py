"""Saving of the cleaned EU life expectancy data"""
from pathlib import Path

import pandas as pd


def save_data(data: pd.DataFrame, output_file: Path) -> None:
    """Save the data to a CSV file."""
    data.to_csv(output_file, index=False)
