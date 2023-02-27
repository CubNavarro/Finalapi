from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from model.reviews import reviewadd


review_api = Blueprint('review_api', __name__, url_prefix='/api/reviewer')


# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(review_api)


class reviewAPI:        
    class _Create(Resource):
        def post(self):
             ''' Read data for json body '''
             body = request.json
             
             ''' Avoid garbage in, error checking '''
            # validate name
             email = body.get('email')
             if email is None or len(email) < 2:
                return {'message': f'email is missing, or is less than 2 characters'}, 210
           
            # look for date, year
             star = body.get('star')
             if star is None or len(star) < 1:
                return {'message': f'star is missing, or is less than 2 characters'}, 210
             reviewtx= body.get('reviewtx')
             if reviewtx is None or len(reviewtx) < 1:
                return {'message': f'review is missing, or is less than 2 characters'}, 210


           
             uo = reviewadd(email, star, reviewtx)
           
             ''' Additional garbage error checking '''
           
           
             review = uo.create()
           
             if review:
                return jsonify(review.read())
            # failure returns error
             return {'message': f'Processed news error'}, 210


    class _Read(Resource):
        def get(self):
            reviews = reviewadd.query.all()    # read/extract all users from database
            json_ready = [reviews.read() for reviews in reviews]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps


    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')