import argparse
from pathlib import Path
import pandas as pd


def load_data() -> pd.DataFrame:
    """
    This function loads the data eu_life_expectancy
    Returns:
        df: eu_life_expectancy as Pandas dataframe 
    """
    path = Path.cwd() / './life_expectancy/data/eu_life_expectancy_raw.tsv'
    df = pd.read_csv(path, sep= r'\,|\t', header=0, engine='python')
    return df


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

    df_cleaned = df[df['region'] == region]

    return df_cleaned

def save_data(df_cleaned: pd.DataFrame, region: str = 'PT') -> None:
    """
    This function saves the cleaned pandas 
    dataframe filtered by the region
    Args:
        df_cleaned: eu_life_expectancy cleaned 
        and filtered by region Pandas DataFrame
        region: Type of Country to filter dataset
    """
    df_cleaned.to_csv(f'./life_expectancy/data/{region.lower()}_life_expectancy.csv', index=False)


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

if __name__ == "__main__": # pragma: no cover
    main()
