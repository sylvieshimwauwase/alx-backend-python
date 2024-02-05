#!/usr/bin/env python3
"""test suite for unittest module task"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """class utils to test access nested maps"""
    @parameterized.expand([
        ({"a":1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])

    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a"), KeyError, "Key 'a' not found in the nested map"),
        ({"a": 1}, ("a", "b"), KeyError, "Key 'b' not found in the nested map"),
    ])

    def test_access_nested_map_exception(self, nested_map, path, expected_exception, expected_message):
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)

class TestGetJson(unittest.TestCase):

    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('utils.requests.get', return_value=mock_response) as mock_get:
            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)

            self.assertEqual(result, test_payload)


class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()

class TestMemoize(unittest.TestCase):

    @patch('utils.TestClass.a_method')
    def test_memoize(self, mock_a_method):
        # Create an instance of TestClass
        test_instance = TestClass()

        # Call a_property twice
        result1 = test_instance.a_property()
        result2 = test_instance.a_property()

        # Assert that a_method was called only once
        mock_a_method.assert_called_once()

        # Assert that the results are correct and the memoization works
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)

if __name__ == "__main__":
    unittest.main()