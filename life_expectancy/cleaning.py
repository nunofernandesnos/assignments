"""Cleaning script for the EU life expectancy data"""
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
INPUT_FILE = DATA_DIR / "eu_life_expectancy_raw.tsv"
OUTPUT_FILE = DATA_DIR / "pt_life_expectancy.csv"
ID_COLUMNS = ["unit", "sex", "age", "region"]


def clean_data() -> None:
    """Load the raw TSV, reshape to long format, clean it and save the PT data."""
    raw = pd.read_csv(INPUT_FILE, sep="\t")

    # First column packs "unit,sex,age,geo\time" into one field
    first_column = raw.columns[0]
    raw[ID_COLUMNS] = raw[first_column].str.split(",", expand=True)
    raw = raw.drop(columns=first_column)

    long = raw.melt(id_vars=ID_COLUMNS, var_name="year", value_name="value")
    long["year"] = long["year"].str.strip().astype(int)
    # Values may carry flags (e.g. "8.6 b") or be ":" when missing
    long["value"] = pd.to_numeric(
        long["value"].str.extract(r"(\d+\.?\d*)", expand=False), errors="coerce"
    )
    long = long.dropna(subset=["value"])

    portugal = long[long["region"] == "PT"]
    portugal.to_csv(OUTPUT_FILE, index=False)
