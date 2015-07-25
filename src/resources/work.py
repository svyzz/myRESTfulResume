from flask.ext.restful import Resource, abort
from flask import jsonify


class Work(Resource):
    """
    This class describes my work experience and since
    I have worked for more than one company AND since
    I don't intend to move this into a UI, this is perhaps
    the right opportunity to adhere to HATEOAS
    """

    def get(self):
        return jsonify({'days/units' : 'm days and n units'})


    def post(self, **kwargs):
        """
        Exit with a 405 since this method is disallowed for this resource
        """
        abort(405)


    def put(self, **kwargs):
        abort(405)


    def delete(self, **kwargs):
        abort(405)
