import pandas as pd
from life_expectancy.strategy import Strategy
from life_expectancy.region import Region

class StrategyFilter(Strategy):
    def run(self, input_path: str = None, input_dataframe: pd.DataFrame = None, input_region: Region = None) -> pd.DataFrame:
        """
        This function filters the dataframe by region
        Args:
            input_path: file path 
            input_dataframe: pandas dataframe to perform the strategy action
            input_region: Region enum to filter the dataframe if defined by the strategy
        Returns:
            df_filtered: pandas dataframe filtered by region
        """
        filter_region = input_region.name

        df_filtered = input_dataframe[input_dataframe['region'] == filter_region].reset_index(drop=True)

        return df_filtered
