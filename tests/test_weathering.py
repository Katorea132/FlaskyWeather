"""
Module to test the Weathering class
"""
import requests
import unittest


basic_url = "http://127.0.0.1:5000/weather"
response = requests.get(basic_url+"?city=medellin&country=co")


class TestWeathering(unittest.TestCase):
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

    # def test_server_answer(self):
    #     """
    #     Tests for the correct welcome message
    #     """
    #     expected_answer = {
    #         "How to use": {
    #             "Required parameters": {
    #                 "City": "A string containing the name of the city",
    #                 "Country": "2 letter country code in lowercase"
    #             },
    #             "Type of Request": "GET",
    #             "Example": "GET /weather?city=$valledupar&country=co&"
    #         }
    #     }
    #     self.assertEqual(expected_answer, response.json(),
    #                      "The server's answer is not what was expected.")

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

    def test_missing_both_params(self):
        """
        Tests for the correct response in case both arguments are missing
        this has the same behaviour as if city was missing
        """
        respon = requests.get(basic_url)
        self.assertEqual(respon.status_code, 400, "Invalid status code")
        self.assertTrue("message" in respon.json(), "No message included")
        self.assertTrue("city" in respon.json()["message"],
                        "No additional info provided")
        self.assertEqual("Please make sure to include a city parameter, \
this is not case sensitive",
                         respon.json()["message"]["city"],
                         "Incorrect message being displayed")

    def test_missing_country_param(self):
        """
        Tests for the correct response in case the country parameter
        is missing.
        """
        respon = requests.get(basic_url + "?city=pizza")
        self.assertEqual(respon.status_code, 400, "Invalid status code")
        self.assertTrue("message" in respon.json(), "No message included")
        self.assertTrue("country" in respon.json()["message"],
                        "No additional info provided")
        self.assertEqual("Please make sure to include a country \
code parameter, in lower case and limited to only 2 characters",
                         respon.json()["message"]["country"],
                         "Incorrect message being displayed")

    def test_incorrect_country_param(self):
        """
        Tests for the correct server response in case the country parameter
        is given but not as specified
        """
        respon = requests.get(basic_url + "?city=pizza&country=asd")
        self.assertEqual(respon.status_code, 400, "Invalid status code")
        self.assertTrue("message" in respon.json(), "No message included")
        self.assertTrue("country" in respon.json()["message"],
                        "No additional info provided")
        self.assertEqual("Please make sure to include a country \
code parameter, in lower case and limited to only 2 characters",
                         respon.json()["message"]["country"],
                         "Incorrect message being displayed")
        respon = requests.get(basic_url + "?city=pizza&country=CO")
        self.assertEqual(respon.status_code, 400, "Invalid status code")
        self.assertTrue("message" in respon.json(), "No message included")
        self.assertTrue("country" in respon.json()["message"],
                        "No additional info provided")
        self.assertEqual("Please make sure to include a country \
code parameter, in lower case and limited to only 2 characters",
                         respon.json()["message"]["country"],
                         "Incorrect message being displayed")
        respon = requests.get(basic_url + "?city=pizza&country=1co2")
        self.assertEqual(respon.status_code, 400, "Invalid status code")
        self.assertTrue("message" in respon.json(), "No message included")
        self.assertTrue("country" in respon.json()["message"],
                        "No additional info provided")
        self.assertEqual("Please make sure to include a country \
code parameter, in lower case and limited to only 2 characters",
                         respon.json()["message"]["country"],
                         "Incorrect message being displayed")
        respon = requests.get(basic_url + "?city=pizza&country=12")
        self.assertEqual(respon.status_code, 400, "Invalid status code")
        self.assertTrue("message" in respon.json(), "No message included")
        self.assertTrue("country" in respon.json()["message"],
                        "No additional info provided")
        self.assertEqual("Please make sure to include a country \
code parameter, in lower case and limited to only 2 characters",
                         respon.json()["message"]["country"],
                         "Incorrect message being displayed")
        respon = requests.get(basic_url + "?city=pizza&country=")
        self.assertEqual(respon.status_code, 400, "Invalid status code")
        self.assertTrue("message" in respon.json(), "No message included")
        self.assertTrue("country" in respon.json()["message"],
                        "No additional info provided")
        self.assertEqual("Please make sure to include a country \
code parameter, in lower case and limited to only 2 characters",
                         respon.json()["message"]["country"],
                         "Incorrect message being displayed")
