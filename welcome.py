"""
This module contains the information to display on the welcome
route
"""
from flask_restful import Resource


class Welcome(Resource):
    """In charge of the root route, only displays basic information
    """
    def get(self):
        """Gives basic information about how the weather endpoint
        works
        """
        return {
            "How to use": {
                "Required parameters": {
                    "City": "A string containing the name of the city",
                    "Country": "2 letter country code in lowercase"
                },
                "Type of Request": "GET",
                "Example": "GET /weather?city=$valledupar&country=co&"
            }
        }
