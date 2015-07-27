from flask.ext.restful import Resource, abort
from flask import jsonify


class About(Resource):
    """
    This class describes what this effort is all about!
    It also lists all of the RESTful endpoints
    """

    def get(self):
        return jsonify({
            'about' : 'a feeble attempt at making my resume RESTful',
            'base_URL' : 'https://svyzz.herokuapp.com/api'
            'endpoints' : '/education, /github, /work, /contact',
            'suggestions and critiques' : 'please drop me a line on GitHub'
        })

    def post(self, **kwargs):
        """
        Exit with a 405 since this method is disallowed for this resource
        """
        abort(405)


    def put(self, **kwargs):
        abort(405)


    def delete(self, **kwargs):
        abort(405)
