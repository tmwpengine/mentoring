from unittest import TestCase
from unittest.mock import patch

from helper_functions import add_five, add_five_to_random_int_less_than_ten


class TestHelperFunctions(TestCase):

    def setUp(self):
        self.num_to_pass = 2

    def test_add_five_function_returns_expected_value_when_negative_integer_passed_in(self):

        # Arrange
        self.num_to_pass = -2
        expected_value = 3

        # Act
        actual_value = add_five(self.num_to_pass)

        # Assert
        self.assertEqual(expected_value, actual_value)

    def test_add_five_function_returns_expected_value(self):
        # Arrange
        expected_value = 7

        # Act
        actual_value = add_five(self.num_to_pass)

        # Assert
        self.assertEqual(expected_value, actual_value)

    def test_add_five_function_raises_exception_when_non_int_value_passed(self):
        self.num_to_pass = "test"

        with self.assertRaises(TypeError):
            add_five(self.num_to_pass)

    @patch("helper_functions.get_random_number_less_than_ten")
    def test_add_five_to_random_int_less_than_ten(self, mock_func):
        mock_func.return_value = 10
        actual_value = add_five_to_random_int_less_than_ten()
        self.assertEqual(15, actual_value)

    def tearDown(self):
        pass