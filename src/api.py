from flask import Flask
from flask.ext import restful
from resources.about import About
from resources.education import Education
from resources.projects import GitHub
from resources.work import OrganizationList, Organizations
from resources.contact import Contact


app = Flask(__name__)
api = restful.Api(app)


"""
Each of the individual resources go here;
This gives us a comprehensive list of all of the
routes and resources and configures our API
"""
api.add_resource(About, '/', '/about')
api.add_resource(Education, '/education')
api.add_resource(GitHub, '/github')
api.add_resource(OrganizationList, '/work')
api.add_resource(Organizations, '/work/<string:org_id>')
api.add_resource(Contact, '/contact')

"""
Run this app in debug mode so that it automatically
restarts after every code change and prints useful messages for us!
"""
if __name__ == '__main__':
    app.run(debug=True)
