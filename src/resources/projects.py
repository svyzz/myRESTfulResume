from flask.ext.restful import Resource, abort
from flask import jsonify
import requests


class GitHub(Resource):
    """
    See documentation for the GET request below!
    """

    def get(self):
        """
        This method makes a call to the standard GitHub API and simply
        forwards the response through.

        Attempting to return a '504 - Gateway Timeout' on
        either a connection or timeout error!
        """
        try:
            response = requests.get('https://api.github.com/users/svyzz').json()
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            abort(504)

        return jsonify(response)


    def post(self, **kwargs):
        """
        Exit with a 405 since this method is disallowed for this resource
        """
        abort(405)


    def put(self, **kwargs):
        abort(405)


    def delete(self, **kwargs):
        abort(405)
