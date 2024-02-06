"""Tests for the cleaning module"""
from unittest import mock
import pandas as pd
from life_expectancy.load_module import load_data
from life_expectancy.save_module import save_data
from life_expectancy.cleaning import clean_data
from life_expectancy.region import Region
from . import OUTPUT_DIR, FIXTURES_DIR


def test_load_data(eu_life_expectancy_path):
    """Run the `load_data` function and compare the output to the expected output"""
    result_df = load_data(eu_life_expectancy_path)
    expected_df = pd.read_csv(eu_life_expectancy_path, sep=r'\,|\t', engine='python')
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_clean_data(eu_life_expectancy_path, pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    df = load_data(eu_life_expectancy_path)
    pt_life_expectancy_result = clean_data(df, Region.PT)
    pd.testing.assert_frame_equal(
        pt_life_expectancy_result, pt_life_expectancy_expected
    )

 #life_expectancy.save_module.pd.DataFrame.to_csv
def test_save_data(eu_life_expectancy_path, pt_life_expectancy_expected):
    """Run the `save_data` function and compare the output to the expected output"""
    with mock.patch('pandas.DataFrame.to_csv') as to_csv_mock:
        to_csv_mock.return_value = print("CSV Saved Successfully")
        df = load_data(eu_life_expectancy_path)
        df_cleaned = clean_data(df, Region.PT)
        save_data(df_cleaned, OUTPUT_DIR / "pt_life_expectancy.csv")
        to_csv_mock.assert_called_once()
        pd.testing.assert_frame_equal(pd.read_csv(OUTPUT_DIR / "pt_life_expectancy.csv"),
                                  pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv"))

def test_region_list(expected_countries_list):
    """Run get country region and compare the output with the expected"""
    result_countries_list = Region.get_country_regions()
    assert result_countries_list == expected_countries_list, "Countries list is incorrect"

