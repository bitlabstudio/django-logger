"""Tests for the Utilities of the ``logger`` app."""
from django.test import TestCase

from logger.models import ActionParameter, Log
from logger.utils import Logger


class LoggerTestCase(TestCase):
    """Tests for the ``Logger`` class."""
    longMessage = True

    def setUp(self):
        self.data = {'test_type1': 'val1', 'test_type2': 'val2'}

    def test_creates_log(self):
        """Test if ``create_log`` creates logs."""
        logger = Logger()
        logger.create_log('test_action', self.data)

        self.assertEqual(Log.objects.all().count(), 1, msg=(
            '``create_log`` created the wrong amount of logs'))
        self.assertEqual(
            ActionParameter.objects.all().count(), len(self.data), msg=(
                '``create_log`` created the wrong amount of action parameters.'
            ))
