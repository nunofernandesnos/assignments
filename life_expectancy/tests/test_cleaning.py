"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy import cleaning
from life_expectancy.cleaning import clean_data, load_data, main, save_data
from . import OUTPUT_DIR


def test_clean_data(pt_life_expectancy_expected):
    """Run `main` and compare the output file to the expected output"""
    main()
    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )


def test_clean_data_other_region(tmp_path, monkeypatch):
    """Run `main` for a non-default region and check the output file"""
    monkeypatch.setattr(cleaning, "DATA_DIR", tmp_path)
    main("FR")
    fr_life_expectancy = pd.read_csv(tmp_path / "fr_life_expectancy.csv")
    assert not fr_life_expectancy.empty
    assert set(fr_life_expectancy["region"]) == {"FR"}


def test_load_clean_save(tmp_path, pt_life_expectancy_expected):
    """Each step works on its own: load, clean in memory, then save"""
    cleaned = clean_data(load_data())
    pd.testing.assert_frame_equal(
        cleaned.reset_index(drop=True), pt_life_expectancy_expected
    )
    output_file = tmp_path / "out.csv"
    save_data(cleaned, output_file)
    pd.testing.assert_frame_equal(
        pd.read_csv(output_file), pt_life_expectancy_expected
    )
