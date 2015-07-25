from flask.ext.restful import Resource, abort
from flask import jsonify


class Education(Resource):
	
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