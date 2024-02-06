import pandas as pd
from abc import ABC, abstractmethod
from life_expectancy.region import Region

class Strategy(ABC):
    """Abstract base class to implement each strategy"""
    @abstractmethod
    def run(self, 
            input_path: str= None, 
            input_dataframe: pd.DataFrame = None, 
            input_region: Region = None):
        """
        Base function
        Args:
            input_path: file path 
            input_dataframe: pandas dataframe to perform the strategy action
            input_region: Region enum to filter the dataframe if defined by the strategy
        """
        pass
