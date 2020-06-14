import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Movie , Actor ,setup_db
from flask_moment import Moment

def create_app(test_config=None):
  # create and configure the app --heroku config --app
  # testing again
  app = Flask(__name__)
  CORS(app)
  moment = Moment(app)
  app.config.from_object('config')
  setup_db(app)
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Contro-Allow-Headers','Content-Type ,Authorization')
    response.headers.add('Access-Contro-Allow-Headers','GET, POST ,PATCH , DELETE ,OPTIONS')
    response.headers.add('Access-Control-Allow-Origin' ,  'http://localhost:5000')
    return response 
  
  @app.route('/test', methods=['GET'])
  def test_api():
    return jsonify({
      'success': True ,
      'message' : "hello world "
    })

  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)