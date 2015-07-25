from flask.ext.restful import Resource, abort
from flask import jsonify


class Education(Resource):
    """
    This class lists my educational qualifications in
    chronological order (not that it matters since I only have
    ONE engineering degree!)

    However, if I did have more, I should perhaps list them all in
    a dictionary and make this adhere to HATEOAS (like /work?)
    """

    def get(self):
        return jsonify({
            'degree' : 'Bachelors in Engineering',
            'major' : 'Computer Science and Engineering',
            'university' : 'Visvesvaraya Technological University, Bangalore',
            'year' : '2008'
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
