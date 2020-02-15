import pandas as pd
import numpy as np
import pytest
from pandas.testing import assert_frame_equal
from unittest.mock import patch
import numpy.testing as npt


class TestMainAdd:

    @pytest.fixture
    def target(self):
        from src.myapp.main import add
        return add

    def test_addint(self, target):
        # call
        actual = target(1, 2)

        # verify
        expect = 3
        assert actual == expect

    def test_addstr(self, target):
        # call
        actual = target('abc', 'def')

        # verify
        expect = 'abcdef'
        assert actual == expect

    @pytest.mark.parametrize('a, b, expected',[
        (10, 20, 30),
        (100, 200, 300),
        ('this is ', 'very cool','this is very cool'),
    ])
    def test_add_using_parametrize(self, target, a, b, expected):
        # call
        actual = target(a, b)

        # verify
        assert actual == expected


class TestMainSub:

    @pytest.fixture
    def target(self):
        from src.myapp.main import sub
        return sub

    @pytest.mark.parametrize(
        'input, expect',
        (
            ((2, 1), 1),
            ((3, 5), -2),
            ((0, 9), -9),
        )
    )
    def test_subint(self, input, expect, target):
        actual = target(*input)
        assert actual == expect, '{}.{}関数いけてねえ'.format(target.__module__, target.__name__)

    def test_typeerror(self, target):
        with pytest.raises(TypeError):
            target('abc', 'def')

    def _test_dict_stub():
        from src.myapp.main import dict_stub as target

        assert target() == {
            'name': 'Takayuki',
            'age': [1, 2, 4, 5],
            'work': {'sphinx': 'committer', 'pyconjp': 'committer'}
        }


class TestClassB:

    @pytest.fixture
    def target(self):
        from src.myapp.main import ClassB
        b = ClassB()
        return b.get_my_df

    @pytest.fixture
    def expected(self):
        return pd.DataFrame(np.arange(9).reshape(3, 3))

    def test_get_my_df(self, expected, target):
        target = target()
        # pandas.DataFrame同士が同一か確認する関数
        assert_frame_equal(target, expected)

        # numpyのarrayが同一か確認する関数
        npt.assert_array_equal(target, expected)
