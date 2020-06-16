import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor


class CapstoneTest(unittest.TestCase):
    """This class represents the Capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = "postgres://cyusdufwqepfbx:86ff10ea3963bed3ba9a8867168c5e727023c041cd42de3751ff9590ed2c8867@ec2-54-86-170-8.compute-1.amazonaws.com:5432/ddp273p1s8o4pj"
        setup_db(self.app, self.database_path)
        self.casting_assistant = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxpajVKQUxRNlBZN1p2NFhJM09zeiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtdHJ5LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU3ZWM3ODJlZTcyZjAwMTNkOTM2MWYiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MjMyOTU2OSwiZXhwIjoxNTkyNDE1OTY5LCJhenAiOiJSc09YY2xiRk1yTzVhcE5VY1g3OVhEWXFjRzhINmU4QyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJzZWFyY2g6YWN0b3IiLCJzZWFyY2g6bW92aWUiXX0.pMAJT54OzFSVghhpLBqLXtDjNMCQuRiWYsmATQZjyhSbX7ddlbqVOjfx97Oauui-kxQ5V42NRMz9pyy9tRxY49hRclk8OXFXRC75K70gJ0bsJWFAkflmfrnqWdygZoR1FD-NIYwJcLpjWSvC7UuywEleTx4HChcR81OEtjqHHqUQzoYcOZp8nIhhpL97bMF4Qfmcmuc4pAlL2qdq7FKWBwhOPaN3igESN5rRoE8g_Lm1yQzABzlg8-v-3a4Q8WxdX6yXmcuq6oZ8uwZZy5lNqEKiVvZEh4on9y-Vg5VYtQ_u29aKYBe0-pI1ojoutROBiWhuTgi1AXvFENJHDWhxaw"
        self.casting_director = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxpajVKQUxRNlBZN1p2NFhJM09zeiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtdHJ5LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU3ZWNhMmM3MGViMDAwMTkzNDFlZGQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MjMyOTcwOCwiZXhwIjoxNTkyNDE2MTA4LCJhenAiOiJSc09YY2xiRk1yTzVhcE5VY1g3OVhEWXFjRzhINmU4QyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInNlYXJjaDphY3RvciIsInNlYXJjaDptb3ZpZSJdfQ.kRz-T1NKGOUwYj_6UnCuZ-evNZymrBNfLfRMoo_04jPpauYJqwTTWC5b0vRXiH55TlXvPy4BNeFJ-RlyC7df7qKplRBNBLn8JqwyVGFTH1XMcr79If1STDebwy8VPJKnXAQMGwBY-dG1DexxyuJ7vdyo8s0zHx6_WCYQzq54LcmWqQjv60YV3qpMOuRsa1911scSXz2HmDoQGjQA1RqajYuRlBR3P8WOF-TQr3JBqdxY1LnQjcUtedcAh3O4BIC5cL5NXyzjgEdES8lLKQAM-UFuj8q5M_37At8BNueUoocGBBjAnJde2dsgiy4RJadD2XM9c_ka-YeHEkSf5geIPQ"
        self.excecutive_producer = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxpajVKQUxRNlBZN1p2NFhJM09zeiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtdHJ5LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU3ZWNjNjkyMmQxMzAwMTkxOTZiMTAiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MjMwNjgxOCwiZXhwIjoxNTkyMzkzMjE4LCJhenAiOiJSc09YY2xiRk1yTzVhcE5VY1g3OVhEWXFjRzhINmU4QyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiLCJzZWFyY2g6YWN0b3IiLCJzZWFyY2g6bW92aWUiXX0.de9UspBwhGamIxPOConJS8DxksA_EMzRTz1eI-ZBRDXYKQKK9OBES65YZXHAsrVPmywAOhWLL8duQbG3Ai-1R_K1NlpFrb80yDXm7633nN3dXfw2_s05AVTqdEik_TgRqCYF73f131NIk39EBxblIqoeuXW9ZSz1JZe-A4EWLuIKNaBkNRecStfinzReZjkFR4e9swJySMryRK_wcxDdqT-Eix8TfWIS1WolGk7cE0ijp41hDIyiQMEFg_oAQRjgmBnZ1yLnkn8DrFuKqpOR0yi8C0RLxue5msb7L_f_VKzZ8jJfVgi0SHCFDEo9HaDEQGbjggBHScGw623-bio0ng"


        self.new_actor = {
            'name': 'Will Smith ? ',
            'age' : 51,
            'gender' : 'male'
        }
        
        self.new_movie = {
            'title' : 'the pursuit of happiness',
            'city' : 'LA',
            'release_date' : '12-12-1212'
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
        'Bearer ' + self.casting_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors']) 
        self.assertTrue(len(data['total_actors']))  

    def test_get_movies(self):
        res = self.client().get('/movies',headers={'Authorization':
        'Bearer ' + self.casting_assistant})
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
        res = self.client().post('/actors',json = self.new_actor,headers={'Authorization':
        'Bearer ' +self.casting_assistant})
        
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
        res = self.client().post('/movies', json = self.new_movie,headers={'Authorization':
        'Bearer ' +self.casting_director})
        
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_actor(self):
        res = self.client().delete('/actors/1',headers={'Authorization':
        'Bearer ' + self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_actor_id'], 3)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['total_actors']))

    def test_delete_actor_fail(self):
        res = self.client().delete('/actors/1',headers={'Authorization':
        'Bearer ' + self.casting_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movie(self):
        res = self.client().delete('/movies/1',headers={'Authorization':
        'Bearer ' +self.excecutive_producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_movie_id'], 3)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['total_movies']))

    def test_delete_movie_fail(self):
        res = self.client().delete('/movies/1',headers={'Authorization':
        'Bearer ' +self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_edit_actor(self):
        res = self.client().patch('/actors/4', json={
            'name':'john smith',
            'age':15,
            'gender':'female'
        },headers={'Authorization':
        'Bearer ' +self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['editied_actor_id'], 4)
        self.assertTrue(data['actors'])
        self.assertTrue(len(data['total_actors']))

    def test_edit_actor_fail(self):
        res = self.client().patch('/actors/4', json={
            'name':'john smith',
            'gender':'female',
            'age':5
        },headers={'Authorization':
        'Bearer ' +self.casting_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_edit_movie(self):
        res = self.client().patch('/movies/4', json={
            'title':'pursument',
            'city':'LA',
            'release_date':'12-12-1212'
        },headers={'Authorization':
        'Bearer ' +self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['edited_movie_id'], 4)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['total_movies']))

    def test_edit_movie_fail(self):
        res = self.client().patch('/movies/1', json={
            'title':'pursument',
            'city':'LA',
            'release_date':'12-12-1212'
        },headers={'Authorization':
        'Bearer ' +self.casting_assistant})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_search_actor(self):
        res = self.client().post('/searchActors', json={
            'name':'will'
        },headers={'Authorization':
        'Bearer ' +self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['matches'])
        self.assertTrue(len(data['number_of_matches']))

    def test_search_actor_fail(self):
        res = self.client().post('/searchActors', json={
            'title':'will'
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_search_movie(self):
        res = self.client().post('/searchMovies', json={
            'title':'will'
        },headers={'Authorization':
        'Bearer ' +self.casting_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['matches'])
        self.assertTrue(data['number_of_matches'])

    def test_search_movie_fail(self):
        res = self.client().post('/searchMovies', json={
            'name':'will'
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        

if __name__ == "__main__":
    unittest.main()