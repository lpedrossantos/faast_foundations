import pandas as pd
from pathlib import Path

def load_data() -> pd.DataFrame:
    """
    This function loads the data eu_life_expectancy
    Returns:
        df: eu_life_expectancy as Pandas dataframe 
    """
    path = Path.cwd() / './life_expectancy/data/eu_life_expectancy_raw.tsv'
    df = pd.read_csv(path, sep= r'\,|\t', header=0, engine='python')
    return df

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
