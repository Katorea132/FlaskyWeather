"""
This module contains the logic related to flask to
return the weather information
"""
from flask_restful import Resource, reqparse, inputs
from api_bridge import bridge


location_args = reqparse.RequestParser()
location_args.add_argument("city", type=str, help="Please make sure to \
include a city parameter, this is not case sensitive", required=True)
location_args.add_argument("country", type=inputs.regex(r"^[a-z]{2}$"),
                           help="Please make sure to include a country code \
parameter, in lower case and limited to only 2 characters", required=True)


class Weathering(Resource):
    """
    Resource to be routed for the weather api
    """
    def get(self):
        answer = bridge(location_args.parse_args())
        return answer[0], answer[1]
