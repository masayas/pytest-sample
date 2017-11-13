import numpy as np
import pandas as pd
import logging


def add(a, b):
    """
    この関数は a + b の結果を返します
    例:

    >>> add(1, 2)
    3

    >>> add('abc', 'def')
    'abcdef'

    以上
    """
    return a + b


def sub(a, b):
    return a - b


def dict_stub():
    return {
        'name': 'Takayuki',
        'age': [1, 2, 3, 4, 5],
        'work': {'sphinx': 'committer', 'pyconjp': 'committee'}
    }


class ClassA:
    def __init__(self):
        self.logger = logging.getLogger()


class ClassB(ClassA):
    def __init__(self):
        super().__init__()
        self.df = pd.DataFrame()

    def get_my_df(self):
        df = pd.DataFrame(np.arange(9).reshape(3, 3))
        return df

    def update_my_df(self):
        self.df = self.get_my_df()
