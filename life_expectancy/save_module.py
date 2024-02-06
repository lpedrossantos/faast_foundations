import pandas as pd

def save_data(df_cleaned: pd.DataFrame, save_path: str) -> None:
    """
    This function saves the cleaned pandas 
    dataframe filtered by the region
    Args:
        df_cleaned: eu_life_expectancy cleaned 
        and filtered by region Pandas DataFrame
        save_path: path to save dataframe
    """
    df_cleaned.to_csv(save_path, index=False)
