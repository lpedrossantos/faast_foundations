from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def run(self, input_path=None, input_dataframe=None, input_region=None):
        pass