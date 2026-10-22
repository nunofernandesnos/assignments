"""Cleaning script for the EU life expectancy data"""
import argparse
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
INPUT_FILE = DATA_DIR / "eu_life_expectancy_raw.tsv"
DEFAULT_REGION = "PT"
ID_COLUMNS = ["unit", "sex", "age", "region"]


def load_data(input_file: Path = INPUT_FILE) -> pd.DataFrame:
    """Load the raw TSV data."""
    return pd.read_csv(input_file, sep="\t")


def clean_data(raw: pd.DataFrame, region: str = DEFAULT_REGION) -> pd.DataFrame:
    """Reshape the raw data to long format, clean it and select one region."""
    # First column packs "unit,sex,age,geo\time" into one field
    first_column = raw.columns[0]
    raw = raw.copy()
    raw[ID_COLUMNS] = raw[first_column].str.split(",", expand=True)
    raw = raw.drop(columns=first_column)

    long = raw.melt(id_vars=ID_COLUMNS, var_name="year", value_name="value")
    long["year"] = long["year"].str.strip().astype(int)
    # Values may carry flags (e.g. "8.6 b") or be ":" when missing
    long["value"] = pd.to_numeric(
        long["value"].str.extract(r"(\d+\.?\d*)", expand=False), errors="coerce"
    )
    long = long.dropna(subset=["value"])

    return long[long["region"] == region]


def save_data(data: pd.DataFrame, output_file: Path) -> None:
    """Save the data to a CSV file."""
    data.to_csv(output_file, index=False)


def main(region: str = DEFAULT_REGION) -> None:
    """Load, clean and save the life expectancy data of a region."""
    raw = load_data()
    cleaned = clean_data(raw, region)
    save_data(cleaned, DATA_DIR / f"{region.lower()}_life_expectancy.csv")


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description="Clean the EU life expectancy data")
    parser.add_argument(
        "--region", default=DEFAULT_REGION, help="region code (default: PT)"
    )
    main(parser.parse_args().region)
