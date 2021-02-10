"""
Module to test the api_bridge module's functions
"""
import unittest
from unittest.suite import BaseTestSuite
from api_bridge import answer_builder, bridge


class TestApiBridge(unittest.TestCase):
    """Tests both functions of the api_bridge module
    """
    def test_bridge_on_not_found(self):
        """
        Tests the correct message on a unexisting/not findable
        combination of country and city for the openweather API
        """
        answer = bridge({"city": "medallo", "country": "co"})
        self.assertEqual(answer[1], 404, "Bridge didn't properly \
detect a fail status code")
        self.assertEqual(answer[0], "We couldn't find the city 'medallo' \
with the country code 'co'")

    def test_bridge_on_found(self):
        """
        Tests for an adecuated dictionary and status code
        on successful finding
        """
        keys = ['location_name', 'temperature', 'wind',
                'cloudiness', 'pressure', 'humidity',
                'sunrise', 'sunset', 'geo_coordinates',
                'requested_time']
        answer = bridge({"city": "valledupar", "country": "co"})
        self.assertTrue(all(key in answer[0] for key in keys),
                        "Not the correct keys")
        self.assertEqual(answer[0]["location_name"], "Valledupar, CO",
                         "Location name is incorrect")

    def test_builder_on_faulty_dict(self):
        """
        Tests for an error on a different kind of dictionary answer
        """
        self.assertRaises(KeyError, answer_builder, {})
