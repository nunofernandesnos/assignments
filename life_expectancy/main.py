"""Entry point for cleaning and saving life expectancy data."""
import argparse

import pandas as pd

from life_expectancy import clean, load, save
from life_expectancy.region import Region


def main(region: Region = clean.DEFAULT_REGION) -> pd.DataFrame:
    """Load, clean and save the life expectancy data of a region."""
    raw = load.load_data()
    cleaned = clean.clean_data(raw, region)
    output_file = load.DATA_DIR / f"{region.value.lower()}_life_expectancy.csv"
    save.save_data(cleaned, output_file)
    return cleaned


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description="Clean the EU life expectancy data")
    parser.add_argument(
        "--region",
        default=clean.DEFAULT_REGION.value,
        choices=[region.value for region in Region],
        help="region code (default: PT)",
    )
    main(Region(parser.parse_args().region))
