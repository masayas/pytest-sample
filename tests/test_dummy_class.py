"""
Example of
how to use spec, spec_set and
investigate the differences between spec, spec_set, autospec in mock.patch decorator
"""
from unittest.mock import Mock
from unittest import mock
import pytest

from src.myapp.dummy_class import DummyClass


class TestSpecArgs:
    """
    spec will raise AttributeError if you try to access an attribute
    that is not defined on the class,
    while still letting you set non-existent attributes manually.
    """
    def test_spec(self):
        spec_mock = Mock(spec=DummyClass)
        spec_mock.foo()  # returns another Mock instance
        with pytest.raises(AttributeError):
            spec_mock.bar()  # raises AttributeError
        spec_mock.bar = Mock()  # allowed with spec

    def test_spec_set(self):
        spec_set_mock = Mock(spec_set=DummyClass)
        spec_set_mock.foo()  # returns another Mock instance
        with pytest.raises(AttributeError):
            spec_set_mock.bar()  # raises AttributeError
            spec_set_mock.bar = Mock()  # raises AttributeError


class TestMockPatchWithVariousArgs:
    """
    Look at differences between parameters used inside mock.patch decorator
    """
    def test_mock_patch(self):
        with mock.patch('src.myapp.dummy_class.DummyClass') as a_mock:
            a_mock.foo()
            a_mock.bar()  # an attribute that does not exist get created, so no error occurs

    def test_mock_patch_with_spec(self):
        with mock.patch('src.myapp.dummy_class.DummyClass', spec=True) as a_mock:
            a_mock.foo()
            with pytest.raises(AttributeError):
                a_mock.bar()  # With the use of spec=True, raises AttributeError

    def test_mock_patch_with_spec_set(self):
        with mock.patch('src.myapp.dummy_class.DummyClass', spec_set=True) as a_mock:
            a_mock.foo()
            with pytest.raises(AttributeError):
                a_mock.bar()  # With the use of spec_set=True, raises AttributeError

    def test_mock_patch_with_autospec(self):
        with mock.patch('src.myapp.dummy_class.DummyClass', autospec=True) as a_mock:
            a_mock.foo()
            with pytest.raises(AttributeError):
                a_mock.bar()  # With the use of autospec=True, raises AttributeError


class TestDiffBtwSpecAndAutospecOnReturnValue:

    def test_with_spec_set_with_sub_attribute(self):
        with mock.patch('src.myapp.dummy_class.DummyClass', spec_set=True) as a_mock:
            a_mock.foo()
            with pytest.raises(AttributeError):
                a_mock.bar()  # With the use of spec_set=True, raises AttributeError
            a_mock.foo.assert_called_once()
            # The following is the typo, but the powerful mock capability
            # creates a new wrong attribute, so it does not fail.
            # This is very bad!
            a_mock.foo.ass_called_once()

    def test_mock_patch_with_autospec_with_sub_attribute(self):
        with mock.patch('src.myapp.dummy_class.DummyClass', autospec=True) as a_mock:
            a_mock.foo()
            with pytest.raises(AttributeError):
                a_mock.bar()  # With the use of spec_set=True, raises AttributeError
            a_mock.foo.assert_called_once()
            # The following is the typo, and creating the patch with autospec
            # allows the API to be the same with the original object,
            # so because the foo does not have the method, it fails luckily.
            with pytest.raises(AttributeError):
                # AttributeError: Mock object has no attribute 'ass_called_once
                a_mock.foo.ass_called_once()


class TestIfAttributeCanBeMade:
    """
    test if the attribute can be made on each
    """
    def test_mock_patch_with_spec_allowing_mock_attribute(self):
        with mock.patch('src.myapp.dummy_class.DummyClass', spec=True) as a_mock:
            a_mock.bar = Mock()  # allowed with spec

    def test_mock_patch_with_autospec_allowing_mock_attribute(self):
        with mock.patch('src.myapp.dummy_class.DummyClass', autospec=True) as a_mock:
            a_mock.bar = Mock()  # allowed with autospec=True

    def test_mock_patch_with_spec_set_not_allowing_mock_attribute(self):
        with mock.patch('src.myapp.dummy_class.DummyClass', spec_set=True) as a_mock:
            with pytest.raises(AttributeError):
                a_mock.bar = Mock()  # not allowed with spec_set=True


class TestIfAttributeCanBeMadeAfterSealing:
    """
    test how strong the sealing is
    """
    def test_with_spec(self):
        with mock.patch('src.myapp.dummy_class.DummyClass', spec=True) as a_mock:
            a_mock.bar = Mock()  # allowed with spec before sealing
            mock.seal(a_mock)
            # once the mock is sealed,
            # an addition of attributes is not allowed
            with pytest.raises(AttributeError):
                # AttributeError: Cannot set A.another_attribute
                a_mock.another_attribute = Mock()

    def test_with_autospec(self):
        with mock.patch('src.myapp.dummy_class.DummyClass', autospec=True) as a_mock:
            a_mock.bar = Mock()  # allowed with spec before sealing
            mock.seal(a_mock)
            # once the mock is sealed,
            # an addition of attributes is not allowed
            with pytest.raises(AttributeError):
                # AttributeError: Cannot set A.another_attribute
                a_mock.another_attribute = Mock()
