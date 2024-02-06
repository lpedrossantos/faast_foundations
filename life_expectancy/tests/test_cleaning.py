"""Tests for the cleaning module"""
from unittest import mock
import pandas as pd
from life_expectancy.region import Region
from life_expectancy.strategy_load import StrategyLoad
from life_expectancy.strategy_clean import StrategyClean
from life_expectancy.strategy_filter import StrategyFilter
from life_expectancy.strategy_save import StrategySave
from . import OUTPUT_DIR

def test_region_list(expected_countries_list):
    """Run get country region and compare the output with the expected"""
    result_countries_list = Region.get_country_regions()
    assert result_countries_list == expected_countries_list, "Countries list is incorrect"

def test_load_tsv(eu_life_expectancy_tsv_path):
    """Run the `load_tsv` function and compare the output to the expected output"""
    load_strat = StrategyLoad()
    result_df = load_strat.run(input_path=eu_life_expectancy_tsv_path)
    expected_df = pd.read_csv(eu_life_expectancy_tsv_path, sep=r'\,|\t', engine='python')
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_load_json(eu_life_expectancy_json_path):
    """Run the `load_json` function and compare the output to the expected output"""
    load_strat = StrategyLoad()
    result_df = load_strat.run(input_path=eu_life_expectancy_json_path)
    expected_df = pd.read_json(eu_life_expectancy_json_path)
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_clean_data(eu_life_expectancy_tsv_path, eu_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    load_strat = StrategyLoad()
    df = load_strat.run(input_path=eu_life_expectancy_tsv_path)
    clean_strat = StrategyClean()
    result_df = clean_strat.run(input_dataframe=df)
    pd.testing.assert_frame_equal(
        result_df.reset_index(drop=True), eu_life_expectancy_expected
    )

def test_filter_data(eu_life_expectancy_tsv_path, pt_life_expectancy_expected):
    """Run the `filter_data` function and compare the output to the expected output"""
    load_strat = StrategyLoad()
    df = load_strat.run(input_path=eu_life_expectancy_tsv_path)
    clean_strat = StrategyClean()
    df_cleaned = clean_strat.run(input_dataframe=df)
    filter_strat = StrategyFilter()
    result_df = filter_strat.run(input_dataframe=df_cleaned, input_region=Region.PT)
    pd.testing.assert_frame_equal(
        result_df, pt_life_expectancy_expected
    )

def test_save_data(eu_life_expectancy_tsv_path, pt_life_expectancy_expected):
    """Run the `save_data` function and compare the output to the expected output"""
    with mock.patch('pandas.DataFrame.to_csv') as to_csv_mock:
        to_csv_mock.return_value = print("CSV Saved Successfully")
        load_strat = StrategyLoad()
        df = load_strat.run(input_path=eu_life_expectancy_tsv_path)
        clean_strat = StrategyClean()
        df_cleaned = clean_strat.run(input_dataframe=df)
        filter_strat = StrategyFilter()
        result_df = filter_strat.run(input_dataframe=df_cleaned, input_region=Region.PT)
        save_strat = StrategySave()
        save_strat.run(input_dataframe=result_df, input_path=OUTPUT_DIR / "pt_life_expectancy.csv")
        to_csv_mock.assert_called_once()
        pd.testing.assert_frame_equal(
            pd.read_csv(OUTPUT_DIR / "pt_life_expectancy.csv"),
            pt_life_expectancy_expected
        )
