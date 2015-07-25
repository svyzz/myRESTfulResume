from flask.ext.restful import Resource, abort
from flask import jsonify


class Work(Resource):
	
	def get(self):
		return jsonify({'days/units' : 'm days and n units'})


	def post(self, **kwargs):
		abort(405)


	def put(self, **kwargs):
		abort(405)


	def delete(self, **kwargs):
		abort(405)