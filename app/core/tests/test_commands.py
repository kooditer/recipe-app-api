from unittest.mock import patch
from django.test import SimpleTestCase
from psycopg2 import OperationalError as Psycopg2OpError
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCased

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """test commands"""
    def test_wait_for_db_ready(self, patched_check):
        """test waiting for database if database ready"""
        patched_check.return_value = True
        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

