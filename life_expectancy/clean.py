"""Cleaning of the EU life expectancy data"""
import pandas as pd

DEFAULT_REGION = "PT"
ID_COLUMNS = ["unit", "sex", "age", "region"]


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
