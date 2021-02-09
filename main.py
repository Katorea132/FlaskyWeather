from link import app, api
from weathering import Weathering
from welcome import Welcome
from weathering import Weathering
"""
This module reigns the rutes an resources used by the API.
Use the enviroment variable FLASK_ENV to switch between debug
And production mode - Defaults to production
Ex: export FLASK_ENV=development
"""


api.add_resource(Welcome, "/")
api.add_resource(Weathering, "/weather")

if __name__ == "__main__":
    app.run(debug=(app.config['ENV'] == 'development'))
