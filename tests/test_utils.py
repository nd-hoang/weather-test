import unittest
from app.utils import get_number
from app.utils import preprocess_input
from app.utils import is_us_zipcode


class TestUtils(unittest.TestCase):
    def test_get_number_in_dict_successfully(self):
        # Run function
        actual = get_number({"number_field": 8}, "number_field")

        # Check if result has correct value
        self.assertEqual(actual, 8)

    def test_get_number_must_raise_value_error_if_field_name_does_not_exist_in_dict(self):
        # Check exception raised if value of field does not exist
        self.assertRaises(ValueError, lambda: get_number(
            {"some_field": 8}, "number_field"
        ))

    def test__get_number_must_raise_value_error_if_field_value_is_not_a_number(self):
        # Check exception raised if value of field is not a number
        self.assertRaises(ValueError, lambda: get_number(
            {"number_field": "Hello"}, "number_field"
        ))

    def test_preprocess_input_only_keep_lowercase_alphabets_and_number_remain_on_preprocess_input_result(self):
        expect = "shouldigooutside"
        test_value = "Should   I go **outside.????"
        actual = preprocess_input(test_value)
        self.assertEqual(actual, expect)

    # US zip code range from 00501 to 99950
    def test_is_us_zipcode_must_only_return_true_if_input_value_in_valid_range(self):
        self.assertEqual(is_us_zipcode(30076), True)
        self.assertEqual(is_us_zipcode(501), True)
        self.assertEqual(is_us_zipcode(99950), True)
        self.assertEqual(is_us_zipcode(500), False)
        self.assertEqual(is_us_zipcode(99951), False)
        self.assertEqual(is_us_zipcode(0), False)
        self.assertEqual(is_us_zipcode(-1), False)


if __name__ == '__main__':
    unittest.main()
