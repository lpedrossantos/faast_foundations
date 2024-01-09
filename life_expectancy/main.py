import argparse
import pandas as pd
from life_expectancy.load_module import load_data
from life_expectancy.save_module import save_data
from life_expectancy.cleaning import clean_data
def main() -> None:
    """
    This function executes the main steps of
    the script:
    1st: Defines the parser and region argument
    2nd: Loads the data
    3rd: Cleans the Data
    4th: Saves the data
    """
    parser = argparse.ArgumentParser(description='filters data by region.')
    parser.add_argument('--region', action='store', default='PT')
    args, _ = parser.parse_known_args()
    
    df = load_data('./data/eu_life_expectancy_raw.tsv')

    df_cleaned = clean_data(df, args.region)

    save_data(df_cleaned, f'./data/{args.region.lower()}_life_expectancy.csv')

if __name__ == "__main__": # pragma: no cover
   main()
