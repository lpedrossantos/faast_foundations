import pandas as pd
from pathlib import Path
from life_expectancy.strategy import Strategy
from life_expectancy.region import Region

class StrategyLoad(Strategy):
    def _load_json(self, input_path: str) -> pd.DataFrame:
        """
        Loads json file 
        Args
            input_path: file path
        Returns:
            df: loaded dataframe as pandas Dataframe
        """
        df = pd.read_json(input_path)
        return df

    def _load_csv(self, input_path: str) -> pd.DataFrame:
        """
        Loads csv file 
        Args
            input_path: file path
        Returns:
            df: loaded dataframe as pandas Dataframe
        """
        df = pd.read_csv(input_path, header=0)
        return df

    def _load_tsv(self, input_path: str) -> pd.DataFrame:
        """
        Loads tsv file 
        Args
            input_path: file path
        Returns:
            df: loaded dataframe as pandas Dataframe
        """
        df = pd.read_csv(input_path, sep= r'\,|\t', header=0, engine='python')
        return df

    def run(self, input_path: str = None, input_dataframe: pd.DataFrame = None, input_region: Region = None) -> pd.DataFrame:
        """
        Performs the load of data
        Args:
            input_path: file path 
            input_dataframe: pandas dataframe to perform the strategy action
            input_region: Region enum to filter the dataframe if defined by the strategy
        Returns:
            load dataframe 
        """
        accepted_file_extensions = {
            '.tsv': self._load_tsv,
            '.csv': self._load_csv,
            '.json': self._load_json
        }

        file_extension = Path(input_path).suffix

        return accepted_file_extensions[file_extension](input_path)
