from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource, reqparse # used for REST API building
# the class ActivityDay, defined in the corresponding model file for the feature, is being imported for its usage in the api.
from model.review import reviewer

# this is where the blueprint class is defined and the url prefix is set, which is then registered to the app in the main.py file.
review_api = Blueprint('review_api', __name__, url_prefix='/api/review')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(review_api)

# this is the main entry point for the app, with the class reviewAPI. 
class reviewAPI:
    # the _create class is being referred to for the post method, to post the objects.        
    class _Create(Resource):
        def post(self):
             ''' Read data for json body '''
             body = request.json
             
             ''' Avoid garbage in, error checking '''
            # valiaddress name
            
            # here, this handles error checking, as the shortest review in the world is 3 characters, so if the review is less than that, it is deemed invalid and not added to the DB.
             name = body.get('name')
             if name is None or len(name) < 3:
                return {'message': f'name is missing'}, 210
           
            # look for address, fun variables
             email = body.get('email')
             reviewtx = body.get('reviewtx')


             # this sets up the review object
             uo = reviewer(review, address, fun)
           
           
             # this adds the review to the DB (uo.create())
             review = uo.create()
             
             # if the addition was successful, then the review is returned to the user in a readable JSON format.
             if review:
                return jsonify(review.read())
            # failure returns error
             return {'message': f'Processed review error'}, 210
    
    # _Read class, needed for the GET request.     
    class _Read(Resource):
        def get(self):
            review = reviewer.query.all()    # read/extract all review from database
            json_ready = [review.read() for review in review]  # prepares the readable output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
        


    # building the API endpoints. there is a create and read endpoint, to serve for both the GET and POST requests.
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')