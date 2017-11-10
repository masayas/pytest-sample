import pytest


class TestMainAdd:

    def _callFUT(self, x, y):
        from main import add
        return add(x, y)

    def test_addint(self):
        # setup
        # create_test_file('hogehoge.txt')
        # write_test_data('hogehoge.txt', 'hogefuga')

        # call
        actual = self._callFUT(1, 2)

        # verify
        expect = 3
        assert actual == expect

        # tear down
        # delete_test_file('hogehoge.txt')

    def test_addstr(self):
        assert self._callFUT('abc', 'def') == 'abcdef'


class TestMainSub:

    @pytest.fixture
    def target(self):
        from main import sub
        return sub

    @pytest.mark.parametrize(
        'input,expect',
        (
            ((2,1), 1),
            ((3, 5), 2),
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

