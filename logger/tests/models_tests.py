"""Tests for the models of the ``logger`` app."""
from django.test import TestCase

from logger.models import (
    Action,
    ActionParameter,
    ActionParameterType,
    Log,
)


class ActionTestCase(TestCase):
    """Tests for the ``Action`` model."""
    def test_instantiation(self):
        """Testing instantiation of the ``Action`` model."""
        log = Action()
        self.assertTrue(log, msg='If instantiated, this should be True')


class ActionParameterTestCase(TestCase):
    """Tests for the ``ActionParameter`` model."""
    def test_instantiation(self):
        """Testing instantiation of the ``ActionParameter`` model."""
        log = ActionParameter()
        self.assertTrue(log, msg='If instantiated, this should be True')


class ActionParameterTypeTestCase(TestCase):
    """Tests for the ``ActionParameterType`` model."""
    def test_instantiation(self):
        """Testing instantiation of the ``ActionParameterType`` model."""
        log = ActionParameterType()
        self.assertTrue(log, msg='If instantiated, this should be True')


class LogTestCase(TestCase):
    """Tests for the ``Log`` model."""
    def test_instantiation(self):
        """Testing instantiation of the ``Log`` model."""
        log = Log()
        self.assertTrue(log, msg='If instantiated, this should be True')
