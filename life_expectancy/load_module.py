import pandas as pd
from pathlib import Path

def load_data(input_path: str) -> pd.DataFrame:
    """
    This function loads the data eu_life_expectancy
    Args:
        input_path: path to load dataset
    Returns:
        df: eu_life_expectancy as Pandas dataframe 
    """
    # path = Path.cwd() / './life_expectancy/data/eu_life_expectancy_raw.tsv'
    df = pd.read_csv(input_path, sep= r'\,|\t', header=0, engine='python')
    return df
