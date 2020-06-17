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
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432',
                                                       self.database_name)
        # self.database_path = "postgres://cyusdufwqepfbx:86ff10ea3963bed3ba9a8867168c5e727023c041cd42de3751ff9590ed2c8867@ec2-54-86-170-8.compute-1.amazonaws.com:5432/ddp273p1s8o4pj"
        setup_db(self.app, self.database_path)
        self.casting_assistant = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxpajVKQUxRNlBZN1p2NFhJM09zeiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtdHJ5LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU3ZWM3ODJlZTcyZjAwMTNkOTM2MWYiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MjQwOTQwOSwiZXhwIjoxNTkyNDk1ODA5LCJhenAiOiJSc09YY2xiRk1yTzVhcE5VY1g3OVhEWXFjRzhINmU4QyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJzZWFyY2g6YWN0b3IiLCJzZWFyY2g6bW92aWUiXX0.Q5IbMUWY-DPd_tTrWr3QtQgISjJuZ_uXB8a_82ZeHc-PROsIclGIJBvmX6xpTj7ioH6fj89Y0y0spsa8SWzxToMNqu7VMC4XXFOXXu7CjCOseoF0qMqyuTfuDmMevpNUK3tvxl2v9Fhyb_zE48Ra9IBWgpg_o5bxx1t33i1a_4j7gklcmqris93G0jYDGys--sdmiUGNEmSJAWrEhzjHE5xU1UdRZ7PzbHn-l-zNoNh3Bb6YlcT5TzPHYEY1DLZkf4NTXYRR1pwa5k5QNmWwaMS5uX2yMwz2U3qh1pQsi6F6_w5c8slZ7Z24p4GmfNiLsxDnmHjNquZCttD_EkDCWg"
        self.casting_director = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxpajVKQUxRNlBZN1p2NFhJM09zeiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtdHJ5LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU3ZWNhMmM3MGViMDAwMTkzNDFlZGQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MjQwOTQ2MCwiZXhwIjoxNTkyNDk1ODYwLCJhenAiOiJSc09YY2xiRk1yTzVhcE5VY1g3OVhEWXFjRzhINmU4QyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInNlYXJjaDphY3RvciIsInNlYXJjaDptb3ZpZSJdfQ.RF_Ii-8atJpI-nBxocAHEPyEwn72WyepcnQXqb8CSJSQloqpldnOPimFOgWjFqqRdMMktcBwQZm4ysEbQiNKj5LJ5UW92yNZtgqYWsTU1K631B8FWKuVwBxFk6NgxdakRxaPQjptS6WtIuHNrD6ZDhffuS-1uVDumsxejyonzNNmKEbYIk4V8JGIoBCPlkfTbMCf36AshhL_dG9dGBUEhJFg2nOKBZuzl8Q9hEiipf4xhHXZDXXx64A6ony_bd5H0-0CdsI5DnKKAmnWZIxCV0HPsYeJ-u-PSRLywfauYsHgQKzF9frQVQSW_zIE9mgdqiqOoAvP2RCGmMrc7ZKKUw"
        self.excecutive_producer = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxpajVKQUxRNlBZN1p2NFhJM09zeiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtdHJ5LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWU3ZWNjNjkyMmQxMzAwMTkxOTZiMTAiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MjQwOTUwMiwiZXhwIjoxNTkyNDk1OTAyLCJhenAiOiJSc09YY2xiRk1yTzVhcE5VY1g3OVhEWXFjRzhINmU4QyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiLCJzZWFyY2g6YWN0b3IiLCJzZWFyY2g6bW92aWUiXX0.ra2SeOw7h0Wqf1gposrEPaF2E_WWIZhfDudHdymCOZu_dXWKuKcGvu3vTxlt5oBlD931ySGZ3m10Czof4a1nc0NwUnv4--qIl7n4xibBs6gTYm7XKpuhPEkvvKqIHp_3P-9SzO9_JUkITf-BMNGe6pjUDJO-wZCLIkaMWjtpVeXGC909QMmXz-NE-OEOwrwE8YIcnyZyxxRSU10rJSXGMX404egg7HANC_kc1d38fNzTbf80CeBlNI1SYjG9tik7WvzRL3yE5OJlGu7vT18PP9OmZqnwVeH98ANuwzbxyXZwKSfNFeTA_TjDre3i9LSoXT-uilEKoxnKroC7h1EhsQ"

        self.new_actor = {
            'name': 'Will Smith ? ',
            'age': 51,
            'gender': 'male'
        }

        self.new_movie = {
            'title': 'the pursuit of happiness',
            'city': 'LA',
            'release_date': '12-12-1212'
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
        res = self.client().get('/actors', headers={'Authorization':
                                'Bearer ' + self.casting_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
        self.assertTrue((data['total_actors']))

    def test_get_movies(self):
        res = self.client().get('/movies', headers={'Authorization':
                                'Bearer ' + self.casting_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue((data['total_movies']))

    def test_add_actor(self):
        res = self.client().post('/actors', json=self.new_actor,
                                 headers={'Authorization': 'Bearer ' +
                                          self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_actor_fail(self):
        res = self.client().post('/actors', json=self.new_actor,
                                 headers={'Authorization':
                                          'Bearer ' + self.casting_assistant})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_add_movie(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers={'Authorization':
                                          'Bearer ' +
                                          self.excecutive_producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_movie_fail(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers={'Authorization':
                                          'Bearer ' + self.casting_director})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_actor(self):
        res = self.client().delete('/actors/1',
                                   headers={'Authorization':
                                            'Bearer ' + self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_actor_id'], 1)
        self.assertTrue(data['actors'])
        self.assertTrue((data['total_actors']))

    def test_delete_actor_fail(self):
        res = self.client().delete('/actors/1',
                                   headers={'Authorization':
                                            'Bearer ' +
                                            self.casting_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers={'Authorization':
                                   'Bearer ' + self.excecutive_producer})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_movie_id'], 1)
        self.assertTrue(data['movies'])
        self.assertTrue((data['total_movies']))

    def test_delete_movie_fail(self):
        res = self.client().delete('/movies/1', headers={'Authorization':
                                   'Bearer ' + self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_edit_actor(self):
        res = self.client().patch('/actors/4', json={
            'name': 'john smith',
            'age': 15,
            'gender': 'female'
        }, headers={'Authorization':
                    'Bearer ' + self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['editied_actor_id'], 4)
        self.assertTrue(data['actors'])
        self.assertTrue((data['total_actors']))

    def test_edit_actor_fail(self):
        res = self.client().patch('/actors/4', json={
            'name': 'john smith',
            'gender': 'female',
            'age': 5
        }, headers={'Authorization':
                    'Bearer ' + self.casting_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_edit_movie(self):
        res = self.client().patch('/movies/4', json={
            'title': 'pursument',
            'city': 'LA',
            'release_date': '12-12-1212'
        }, headers={'Authorization':
                    'Bearer ' + self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['edited_movie_id'], 4)
        self.assertTrue(data['movies'])
        self.assertTrue((data['total_movies']))

    def test_edit_movie_fail(self):
        res = self.client().patch('/movies/1', json={
            'title': 'pursument',
            'city': 'LA',
            'release_date': '12-12-1212'
        }, headers={'Authorization':
                    'Bearer ' + self.casting_assistant})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_search_actor(self):
        res = self.client().post('/searchActors', json={
            'name': 'will'
        }, headers={'Authorization':
                    'Bearer ' + self.casting_director})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['matches'])
        self.assertTrue((data['number_of_matches']))

    def test_search_actor_fail(self):
        res = self.client().post('/searchActors', json={
            'title': 'will'
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_search_movie(self):
        res = self.client().post('/searchMovies', json={
            'title': 'purs'
        }, headers={'Authorization':
                    'Bearer ' + self.casting_assistant})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['matches'])
        self.assertTrue(data['number_of_matches'])

    def test_search_movie_fail(self):
        res = self.client().post('/searchMovies', json={
            'name': 'will'
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


if __name__ == "__main__":
    unittest.main()
