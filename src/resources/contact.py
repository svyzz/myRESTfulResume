from flask.ext.restful import Resource, abort
from flask import jsonify


class Contact(Resource):
    """
    This class contains my contact and location details
    and a rider asking for my resume if you really want to get in touch!
    """
    
    def get(self):
        return jsonify({
            'email' : '<Ask me for my resume!>',
            'github' : 'https://github.com/svyzz *OR* /github for a smidgeon more detail!',
            'linkedIN' : 'http://tinyurl.com/pq2lrkv',
            'location' : 'Wellington, New Zealand',
            'name' : 'Arun Venkatram',
            'phone number' : '<Ask me for my resume!>'
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
