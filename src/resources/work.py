from flask.ext.restful import Resource, abort
from flask import jsonify


organizations = [
        {
            'organization' : 'Assurity Consulting',
            'location' : 'Wellington, New Zealand',
            'time period' : 'August 2014 - Present',
            'role' : 'Technical Consultant',
            'id' : 'ASC'
        },
        {
            'organization' : 'Apigee India SDC',
            'location' : 'Bangalore, India',
            'time period' : 'April 2013 - July 2014',
            'role' : 'Software Engineer',
            'id' : 'APIC'
        },
        {
            'organization' : 'Amazon.com',
            'location' : 'Bangalore, India',
            'time period' : 'August 2010 - April 2013',
            'role' : 'QA Engineer',
            'id' : 'AMZN'
        },
        {
            'organization' : 'Intel Security Inc.',
            'location' : 'Bangalore, India',
            'time period' : 'January 2009 - August 2010',
            'role' : 'Engineer - Research, AVERT Labs',
            'id' : 'INTC'
        },
        {
            'organization' : 'Akamai Technologies Inc.',
            'location' : 'Bangalore, India',
            'time period' : 'July 2008 - January 2009',
            'role' : 'Associate/Intern',
            'id' : 'AKAM'
        },
        {
            'organization' : 'Freescale Semiconductors',
            'location' : 'Bangalore, India',
            'time period' : 'January 2008 - July 2008',
            'role' : 'College Intern',
            'id' : 'FSL'
        }
    ]


class OrganizationList(Resource):
    """
    This class describes my work experience and since I have worked
    for more than one company AND since I don't intend to move this into a UI,
    this is perhaps the right opportunity to adhere to *some* HATEOAS
    """

    def get(self):
        return {
            'organizations' : [organization['id'] for organization in organizations],
            'addendum' : 'HATEOAS. Yay!',
            'usage' : '/organization/<organization ID> for more details'
        }


    def post(self, **kwargs):
        """
        Exit with a 405 since this method is disallowed for this resource
        """
        abort(405)


    def put(self, **kwargs):
        abort(405)


    def delete(self, **kwargs):
        abort(405)


class Organizations(Resource):
    """
    This class manages how individual endpoints that correspond to
    each of the organizations behave
    """

    def get(self, org_id):
        details = next((organization for organization in organizations if organization['id'] == org_id), None)
        if details == None:
            abort(400)
        return details


    def post(self, **kwargs):
        abort(405)


    def put(self, **kwargs):
        abort(405)


    def delete(self, **kwargs):
        abort(405)