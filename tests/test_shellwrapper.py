import unittest

from bulletsh.Exceptions.invalid_token_exception import InvalidTokenException
from bulletsh.shellwrapper import ShellWrapper


class TestShellWrapper(unittest.TestCase):

    def test_invalid_token(self):
        sw = ShellWrapper("")
        line = "echo test"
        self.assertRaises(InvalidTokenException, lambda: sw.default(line))

    def test_parse_line_secret_success(self):
        sw = ShellWrapper("")
        line = "echo test --secret"
        cmd_list = sw.parse_line(line)
        expected_list = ["echo", "test"]
        self.assertEqual(expected_list, cmd_list)