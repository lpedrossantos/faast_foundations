"""Tests for the cleaning module"""
import pandas as pd
from unittest.mock import patch, Mock

from life_expectancy.cleaning import main
from life_expectancy.load_save_module import load_data
from . import OUTPUT_DIR, FIXTURES_DIR


@patch("life_expectancy.cleaning.pd.read_csv")
def test_load_data(read_csv_mock: Mock):
    read_csv_mock.return_value = pd.DataFrame()
    result_df = load_data()

    read_csv_mock.assert_called_once()

    pd.testing.assert_frame_equal(result_df, pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_expected.csv"))


def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    pt_life_expectancy_expected = main()
    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )


@patch("life_expectancy.cleaning.pd.DataFrame.to_csv")
def test_save_data(to_csv_mock: Mock):
    to_csv_mock.return_value = pd.DataFrame()
    result_df = main()
    result_df.to_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )

    # to_csv_mock.assert_called_once()

    pd.testing.assert_frame_equal(pd.read_csv(OUTPUT_DIR / "pt_life_expectancy.csv"), 
                                  pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv"))
