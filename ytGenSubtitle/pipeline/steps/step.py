from abc import ABC, abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, input_kwargs, temp_data):
        pass


class StepException(Exception):
    pass
