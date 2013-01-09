"""Tests for the Utilities of the ``logger`` app."""
from django.test import TestCase

from logger.models import Log
from logger.utils import Logger


class LoggerTestCase(TestCase):
    """Tests for the ``Logger`` class."""
    def test_creates_log(self):
        """Test if ``create_log`` creates logs."""
        logger = Logger()
        logger.create_log('test_action', 'test_action_type', 'test_value')

        self.assertEqual(Log.objects.all().count(), 1, msg=(
            'When ``create_log`` is called, there should be one log in the'
            ' database.'))
        with self.assertRaises(IndexError):
            logger.create_log('test_action', ['foo', 'bar'], 'value')
        with self.assertRaises(IndexError):
            logger.create_log('test_action', 'foo', ['value1', 'value2'])
