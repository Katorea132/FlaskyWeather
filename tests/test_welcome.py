"""
Module to test the welcome class
"""
import requests
import unittest


basic_url = "http://127.0.0.1:5000/"
response = requests.get(basic_url)


class TestWelcome(unittest.TestCase):
    """Test class used to verify the correct responde on the
    root requests '/'
    """

    def test_content_header(self):
        """
        Tests for the presence of the content-type header
        and it's correct values.
        """
        self.assertTrue("Content-Type" in response.headers,
                        "Content-Type header is not defined")
        self.assertEqual("application/json",
                         response.headers["Content-Type"],
                         "Incorrect content-type set")

    def test_server_answer(self):
        """
        Tests for the correct welcome message
        """
        expected_answer = {
            "How to use": {
                "Required parameters": {
                    "City": "A string containing the name of the city",
                    "Country": "2 letter country code in lowercase"
                },
                "Type of Request": "GET",
                "Example": "GET /weather?city=$valledupar&country=co&"
            }
        }
        self.assertEqual(expected_answer, response.json(),
                         "The server's answer is not what was expected.")

    def test_different_http_methods(self):
        """
        Tests for the correct error message when trying
        an invalid method for the endpoint
        """
        respon = requests.post(basic_url)
        self.assertEqual(respon.status_code, 405, "Invalid status code")
        self.assertTrue("message" in respon.json(), "No message included")
        self.assertEqual("The method is not allowed for the requested URL.",
                         respon.json()["message"], "Not the correct message")
