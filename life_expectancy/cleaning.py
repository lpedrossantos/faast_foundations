import argparse
import pandas as pd
from life_expectancy.load_module import load_data
from life_expectancy.save_module import save_module

def clean_data(df: pd.DataFrame, region: str ='PT') -> pd.DataFrame:
    """
    This function cleans the data from eu_life_expectancy_raw dataset.
    By default filters for the PT region but it can also be filter
    for another region by passing the command line argument --region
    
    Args:
        df: eu_life_expectancy Pandas DataFrame
        region: Type of Country to filter dataset
    
    Returns:
        df_cleaned: dataframe processed
    """
    df = df.melt(id_vars=['unit', 'sex', 'age', 'geo\\time'])

    df = df.rename(columns={'geo\\time' : 'region', 'variable': 'year'})

    #Remove chars and mantain only numeric values without whitespaces
    df.value = df.value.apply(lambda x: None if ':' in x else x)
    df.value = df.value.str.replace(r'[^0-9.]', '', regex=True)

    df = df.astype({'year': int, 'value': float})

    df = df.dropna()

    df_cleaned = df[df['region'] == region].reset_index(drop=True)

    return df_cleaned

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
    
    df = load_data()

    df_cleaned = clean_data(df, args.region)

    save_data(df_cleaned, args.region)

    return df_cleaned

if __name__ == "__main__": # pragma: no cover
   main()
