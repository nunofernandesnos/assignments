"""Entry point for cleaning and saving life expectancy data."""
import argparse

import pandas as pd

from life_expectancy import clean, load, save


def main(region: str = clean.DEFAULT_REGION) -> pd.DataFrame:
    """Load, clean and save the life expectancy data of a region."""
    raw = load.load_data()
    cleaned = clean.clean_data(raw, region)
    output_file = load.DATA_DIR / f"{region.lower()}_life_expectancy.csv"
    save.save_data(cleaned, output_file)
    return cleaned


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description="Clean the EU life expectancy data")
    parser.add_argument(
        "--region", default=clean.DEFAULT_REGION, help="region code (default: PT)"
    )
    main(parser.parse_args().region)
