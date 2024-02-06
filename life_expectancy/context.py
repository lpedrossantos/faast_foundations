from typing import Any
import pandas as pd
from life_expectancy.strategy import Strategy
from life_expectancy.region import Region

class Context:
    """
    This class implements the context obj
    that serves as interface between the strategies
    and application
    """
    def __init__(self) -> None:
        """Constructor class"""
        #private attribute
        self.__strategy = Strategy

    def set_strategy(self, strategy: Strategy) -> None:
        """Set strategy
        Args:
            strategy: Strategy obj
        """
        self.__strategy = strategy

    def get_strategy(self) -> Strategy:
        """
        Gets the current strategy defined
        Returns
            Strategy Obj
        """
        return self.__strategy

    def run_strategy(self, 
                     input_path: str = None,
                     input_dataframe: pd.DataFrame = None,
                     input_region: Region = None) -> Any:
        """
        Executes the defined strategy
        Args:
            input_path: file path 
            input_dataframe: pandas dataframe to perform the strategy action
            input_region: Region enum to filter the dataframe if defined by the strategy
        Returns:
            output of the run method of the defined strategy
        """
        return self.__strategy.run(input_path, input_dataframe, input_region)
