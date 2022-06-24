""" Module Define Pipleline Class."""

from abc import ABC


class Pipeline(ABC):
    """Defines Pipeline Class."""

    def __init__(self):
        """Constructor function of Pipeline Class."""
        self.__source = None

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, generator):
        if self.__source is None:
            self.__source = generator
        else:
            raise Exception('source attribute of pipeline can not be reset')

    def __iter__(self):
        return self.__generator()   

    def __generator(self):
        try:
            while True:
                data = next(self.__source) if self.source else {}
                if self.filter_data(data):
                    yield self.map_data(data)
        except StopIteration:
            return

    def __or__(self, other):
        """Methods for connecting object with other pipleline object."""
        other.source = self.__generator()
        return other

    def filter_data(self, value):
        """Filters data items."""
        return True

    def map_data(self, value):
        """Map data to one form to another."""
        return value