"""Pytest configuration file"""
import json
import pandas as pd
import pytest

from . import FIXTURES_DIR

@pytest.fixture(scope="session")
def eu_life_expectancy_path() -> pd.DataFrame:
    """Fixture to load the expected dataset"""
    return FIXTURES_DIR / "eu_life_expectancy_raw.tsv"

@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")

@pytest.fixture(scope="session")
def expected_countries_list() -> list:
    """Fixture to load expected output countries list"""
    with open(FIXTURES_DIR / 'countries_list.json', 'r', encoding='utf-8') as file:
        loaded_countries_list = json.load(file)
    return loaded_countries_list
