import pytest
from unittest.mock import patch

class TestMainAdd:

    @pytest.fixture
    def target(self):
        from main import add
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


class TestMainSub:

    @pytest.fixture
    def target(self):
        from main import sub
        return sub

    # @patch('main.dummy_func')
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
        from main import dict_stub as target

        assert target() == {
            'name': 'Takayuki',
            'age': [1, 2, 4, 5],
            'work': {'sphinx': 'committer', 'pyconjp': 'committer'}
        }

