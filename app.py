import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Movie, Actor, setup_db
from flask_moment import Moment
from controllers.auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app --heroku config --app
    # testing again
    app = Flask(__name__)
    CORS(app)
    moment = Moment(app)
    app.config.from_object('config')
    setup_db(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    def paginate_actors(request, selection):
        actors_per_page = 10
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * actors_per_page
        end = start + actors_per_page

        actors = [actor.format() for actor in selection]
        current_actors = actors[start:end]

        return current_actors

    def paginate_movies(request, selection):
        movies_per_page = 10
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * movies_per_page
        end = start + movies_per_page

        movies = [movie.format() for movie in selection]
        current_movies = movies[start:end]

        return current_movies

    @app.after_request
    def add_cors_headers(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, PUT, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(jwt):
        selection = list(Actor.query.order_by(Actor.id).all())
        current_actors = paginate_actors(request, selection)

        return jsonify({
            'success': True,
            'actors': current_actors,
            'total_actors': len(selection)
        })

    @app.route('/movies', methods=['GET'])
    # @requires_auth('get:movies')
    def get_movies():
        selection = list(Movie.query.order_by(Movie.id).all())
        current_movies = paginate_movies(request, selection)

        return jsonify({
            'success': True,
            'movies': current_movies,
            'total_movies': len(selection)
        })

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actor')
    def add_actor(jwt):
        body = request.get_json()
        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)

        try:
            actor = Actor(name=new_name, age=new_age,
                          gender=new_gender)
            actor.insert()

            selection = (Actor.query.order_by(Actor.id).all())
            current_actors = paginate_actors(request, selection)

            return jsonify({
                'success': True,
                'created': actor.id,
                'actors': current_actors,
                'total_actors': len(selection)
            })
        except Exception:
            abort(422)

    @app.route('/movies', methods=['POST'])
    # @requires_auth('post:movie')
    def add_movie():
        body = request.get_json()
        new_title = body.get('title', None)
        new_city = body.get('city', None)
        new_release_date = body.get('release_date', None)

        try:
            movie = Movie(title=new_title, city=new_city,
                          release_date=new_release_date)
            movie.insert()

            selection = list(Movie.query.order_by(Movie.id).all())
            current_movies = paginate_movies(request, selection)

            return jsonify({
                'success': True,
                'created': movie.id,
                'movies': current_movies,
                'total_movies': len(selection)
            })

        except Exception:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(jwt, actor_id):
        try:
            actor = Actor.query.filter(Actor.id ==
                                       actor_id).first_or_404()
            actor.delete()

            selection = list(Actor.query.order_by(Actor.id).all())
            current_actors = paginate_actors(request, selection)

            return jsonify({
                'success': True,
                'deleted_actor_id': actor.id,
                'actors': current_actors,
                'total_actors': len(selection)
            })

        except Exception:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    # @requires_auth('delete:movie')
    def delete_movie(movie_id):
        try:

            movie = Movie.query.filter(Movie.id ==
                                       movie_id).first_or_404()
            movie.delete()

            selection = list(Movie.query.order_by(Movie.id).all())
            current_movies = paginate_movies(request, selection)

            return jsonify({
                'success': True,
                'deleted_movie_id': movie.id,
                'movies': current_movies,
                'total_movies': len(selection)
            })
        except Exception:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def edit_actor(jwt, actor_id):
        try:
            actor = Actor.query.filter(Actor.id ==
                                       actor_id).first_or_404()
            body = request.get_json()

            actor.name = body.get('name', None)
            actor.age = body.get('age', None)
            actor.gender = body.get('gender', None)

            actor.update()

            selection = list(Actor.query.order_by(Actor.id).all())
            current_actors = paginate_actors(request, selection)

            return jsonify({
                'success': True,
                'editied_actor_id': actor.id,
                'actors': current_actors,
                'total_actors': len(selection)
            })

        except Exception:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    # @requires_auth('patch:movie')
    def edit_movie(movie_id):
        try:
            movie = Movie.query.filter(Movie.id ==
                                       movie_id).first_or_404()
            body = request.get_json()
            movie.title = body.get('title', None)
            movie.city = body.get('city', None)
            movie.release_date = body.get('release_date', None)

            movie.update()

            selection = list(Movie.query.order_by(Movie.id).all())
            current_movies = paginate_movies(request, selection)

            return jsonify({
                'success': True,
                'edited_movie_id': movie.id,
                'movies': current_movies,
                'total_movies': len(selection)
            })
        except Exception:
            abort(422)

    @app.route('/searchActors', methods=['POST'])
    @requires_auth('search:actor')
    def search_actor(jwt):
        try:

            body = request.get_json()

            if ('name' in body):
                name = body.get('name', None)
                selection = Actor.query.filter(Actor.name.ilike
                                               (f'%{name}%')).all()
                current_actors = paginate_actors(request,
                                                 selection)
            if ('age' in body):
                age = body.get('age', None)
                selection = Actor.query.filter(Actor.age ==
                                               (age))
                current_actors = paginate_actors(request,
                                                 selection)

            return jsonify({
                'success': True,
                'matches': current_actors,
                'number_of_matches': len(current_actors)
            })
        except Exception:
            abort(422)

    @app.route('/searchMovies', methods=['POST'])
    # @requires_auth('search:movie')
    def search_movie(jwt):
        # try:
        body = request.get_json()

        if('title' in body):
            title = body.get('title', None)
            selection = Movie.query.filter(
                Movie.title.ilike(f'%{title}%')).all()
            current_movies = paginate_movies(request,
                                             selection)
        if('city' in body):
            city = body.get('city')
            selection = Movie.query.filter
            (Movie.city.ilike(f'%{city}%')).all()
            current_movies = paginate_movies(request,
                                             selection)
        return jsonify({
            'success': True,
            'matches': current_movies,
            'number_of_matches': len(current_movies)
        })
        # except Exception:
        # abort(422)

    @app.route('/')
    def main_page():
        return jsonify({
            'success': False,
            'message': 'please give the right authorization'
        })

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(500)
    def Internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    @app.errorhandler(AuthError)
    def handle_Auth_Error(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "AuthError"
        }), 401

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
