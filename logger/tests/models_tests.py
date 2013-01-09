"""Tests for the models of the ``logger`` app."""
import decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from logger.models import (
    Action,
    ActionParameter,
    ActionParameterType,
    Log,
)


class ActionTestCase(TestCase):
    """Tests for the ``Action`` model."""
    longMessage = True

    def test_instantiation(self):
        """Testing instantiation of the ``Action`` model."""
        log = Action()
        self.assertTrue(log, msg='If instantiated, this should be True')


class ActionParameterTestCase(TestCase):
    """Tests for the ``ActionParameter`` model."""
    longMessage = True

    def setUp(self):
        self.user = User()
        self.user.save()

    def test_get_and_set_value(self):
        """
        Testing ``get_value`` and ``set_value`` of the ``ActionParameter ``
        model.

        """
        parameter = ActionParameter(value_char='foo')
        # test instantiation
        self.assertTrue(parameter, msg=(
            'If instantiated, this should be True'))

        # testing get_value method
        self.assertEqual(parameter.get_value(), 'foo', msg=(
            'When ``get_value`` is called, the return value should be "foo".'))

        # test set_value method
        new_parameter = ActionParameter()

        # for an object
        new_parameter.set_value(self.user)
        self.assertEqual(new_parameter.get_value(), self.user, msg=(
            'When ``set_value`` is called, it should store the user instance.'
        ))

        # for a decimal
        new_parameter.value_object = None
        new_parameter.set_value(decimal.Decimal('12.34'))
        self.assertEqual(
            new_parameter.get_value(), decimal.Decimal('12.34'), msg=(
                'When ``set_value`` is called, it should store the decimal'
                ' value "12.34".'))

        # for a datetime
        new_parameter.value_decimal = None
        time = timezone.now()
        new_parameter.set_value(time)
        self.assertEqual(new_parameter.get_value(), time, msg=(
            'When ``set_value`` is called, it should store current time.'))

        # for a boolean
        new_parameter.value_time = None
        new_parameter.set_value(True)
        self.assertEqual(new_parameter.get_value(), True, msg=(
            'When ``set_value`` is called, it should store True.'))

        # for a string
        new_parameter.value_bool = None
        new_parameter.set_value('foobar')
        self.assertEqual(new_parameter.get_value(), 'foobar', msg=(
            'When ``set_value`` is called, it should store "foobar".'))

        # for an integer
        new_parameter.value_char = None
        new_parameter.set_value(1337)
        self.assertEqual(new_parameter.get_value(), '1337', msg=(
            'When ``set_value`` is called, it should store 1337 as a string.'))

        # test that get_value return None when nothing is stored
        new_parameter.value_int = None
        self.assertEqual(new_parameter.get_value(), None, msg=(
            'When nothing ist stored, ``get_value`` should return None.'))


class ActionParameterTypeTestCase(TestCase):
    """Tests for the ``ActionParameterType`` model."""
    longMessage = True

    def test_instantiation(self):
        """Testing instantiation of the ``ActionParameterType`` model."""
        parameter_type = ActionParameterType()
        self.assertTrue(parameter_type, msg=(
            'If instantiated, this should be True'))


class LogTestCase(TestCase):
    """Tests for the ``Log`` model."""
    longMessage = True

    def test_instantiation(self):
        """Testing instantiation of the ``Log`` model."""
        log = Log()
        self.assertTrue(log, msg='If instantiated, this should be True')
