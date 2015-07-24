from flask import Flask
from flask.ext import restful
from resources.about import About
from resources.education import Education
from resources.projects import Projects
from resources.work import Work
# Add contact here!


app = Flask(__name__)
api = restful.Api(app)

# Each of the individual resources go here
# This gives us a comprehensive list of all routes and resources and configures our API
api.add_resource(About, '/', '/about')
api.add_resource(Education, '/education')
api.add_resource(Projects, '/projects')
api.add_resource(Work, '/work')

# Run the app in debug mode so it automatically restarts after every code change and prints useful messages!
# This is *NEVER* going to production anyways :D
if __name__ == '__main__':
    app.run(debug=True)