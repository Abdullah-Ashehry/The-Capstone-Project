import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from .app import create_app
from models import setup_db, Movie, Actor


class CapstoneTest(unittest.TestCase):
    """This class represents the Capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.casting_assistant = 'token_value'
        self.casting_director = ''
        self.excecutive_producer = ''


        self.new_actor = {
            'name': 'Will Smith ? ',
            'age' : '51',
            'gender' : 'male',
            'shows_movie' : '4'
        }
        
        self.new_movie = {
            'title' : 'the pursuit of happiness',
            'city' : 'LA',
            'release_date' : '12-12-1212',
            # 'Actor_id' : ''
        }
        
    
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass
    
    def test_get_actors(self):
        res = self.client().get('/actors',headers={'Authorization':
        'Bearer ' +self.casting_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors']) 
        self.assertTrue(len(data['total_actors']))  

    def test_get_movies(self):
        res = self.client().get('/movies',headers={'Authorization':
        'Bearer ' +self.casting_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies']) 
        self.assertTrue(len(data['total_movies']))  

    def test_add_actor(self):
        res = self.client().post('/actors', json = self.new_actor,headers={'Authorization':
        'Bearer ' +self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_actor_fail(self):
        res = self.client().post('/actors', json = {'name': 'Will Smith ? ',
            'age' : '51',
            'gender' : 'male'})
        
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
    
    def test_add_movie(self):
        res = self.client().post('/movies', json = self.new_movie,headers={'Authorization':
        'Bearer ' +self.excecutive_producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_movie_fail(self):
        res = self.client().post('/movies', json = {'name': 'Will Smith ? ',
            'age' : '51',
            'gender' : 'male'})
        
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_actor(self):
        res = self.client().delete('/actors/3',headers={'Authorization':
        'Bearer ' +self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_actor_id'], 3)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['total_actors']))

    def test_delete_actor_fail(self):
        res = self.client().delete('/actors/100000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movie(self):
        res = self.client().delete('/movies/3',headers={'Authorization':
        'Bearer ' +self.excecutive_producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_movie_id'], 3)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['total_movies']))

    def test_delete_movie_fail(self):
        res = self.client().delete('/movies/100000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_edit_actor(self):
        res = self.client().patch('/actors/1', json={
            'name':'john smith',
            'age':'15',
            'gender':'female',
            'shows_movie':'5'
        },headers={'Authorization':
        'Bearer ' +self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['edited_actor_id'], 1)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['total_actors']))

    def test_edit_actor_fail(self):
        res = self.client().patch('/actors/1', json={
            'name':'john smith',
            'gender':'female',
            'shows_movie':'5'
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_edit_movie(self):
        res = self.client().patch('/movies/1', json={
            'name':'john smith',
            'age':'15',
            'gender':'female',
            'shows_movie':'5'
        },headers={'Authorization':
        'Bearer ' +self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['edited_movie_id'], 1)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['total_movies']))

    def test_edit_movie_fail(self):
        res = self.client().patch('/movies/1', json={
            'name':'john smith',
            'gender':'female',
            'shows_movie':'5'
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_search_actor(self):
        res = self.client().post('/searchActor', json={
            'name':'will'
        },headers={'Authorization':
        'Bearer ' +self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['matches'])
        self.assertTrue(len(data['number_of_matches']))

    def test_search_actor_fail(self):
        res = self.client().post('/searchActor', json={
            'title':'will'
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_search_movie(self):
        res = self.client().post('/searchMovie', json={
            'title':'will'
        },headers={'Authorization':
        'Bearer ' +self.casting_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['matches'])
        self.assertTrue(len(data['number_of_matches']))

    def test_search_movie_fail(self):
        res = self.client().post('/searchMovie', json={
            'name':'will'
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        

if __name__ == "__main__":
    unittest.main()