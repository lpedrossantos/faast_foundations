import pandas as pd
from life_expectancy.region import Region
from life_expectancy.strategy import Strategy

class StrategyClean(Strategy):
    """
    This class inherits from abstract class strategy
    and it implements the cleaning data strategy.
    """
    def run(self, 
            input_path: str = None, 
            input_dataframe: pd.DataFrame = None, 
            input_region: Region = None) -> pd.DataFrame:
        """
        Performs the cleaning steps of dataframe
        Args:
            input_path: file path 
            input_dataframe: pandas dataframe to perform the strategy action
            input_region: Region enum to filter the dataframe if defined by the strategy
        Returns:
            df: pandas dataframe cleaned
        """
        df = input_dataframe.melt(id_vars=['unit', 'sex', 'age', 'geo\\time'])

        df = df.rename(columns={'geo\\time' : 'region', 'variable': 'year'})

        #Remove chars and mantain only numeric values without whitespaces
        df.value = df.value.apply(lambda x: None if ':' in x else x)
        df.value = df.value.str.replace(r'[^0-9.]', '', regex=True)

        df = df.astype({'year': int, 'value': float})

        df = df.dropna()

        return df
