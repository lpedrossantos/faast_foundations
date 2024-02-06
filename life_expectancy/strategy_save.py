import pandas as pd
from life_expectancy.strategy import Strategy
from life_expectancy.region import Region

class StrategySave(Strategy):
    def run(self, input_path: str = None, input_dataframe: pd.DataFrame = None, input_region: Region = None) -> pd.DataFrame:
        """
        This function saves the dataframe
        Args:
            input_path: file path 
            input_dataframe: pandas dataframe to perform the strategy action
            input_region: Region enum to filter the dataframe if defined by the strategy
        """
        input_dataframe.to_csv(input_path, index=False)
