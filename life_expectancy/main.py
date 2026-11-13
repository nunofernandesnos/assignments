"""Entry point for cleaning and saving life expectancy data."""
import argparse

from life_expectancy import cleaning


def main(region: str = cleaning.DEFAULT_REGION) -> None:
    """Load, clean and save the life expectancy data of a region."""
    raw = cleaning.load_data()
    cleaned = cleaning.clean_data(raw, region)
    output_file = cleaning.DATA_DIR / f"{region.lower()}_life_expectancy.csv"
    cleaning.save_data(cleaned, output_file)


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description="Clean the EU life expectancy data")
    parser.add_argument(
        "--region", default=cleaning.DEFAULT_REGION, help="region code (default: PT)"
    )
    main(parser.parse_args().region)