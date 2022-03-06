# The-Capstone-Project
F.S.N.D Graduation Project

# Motivation : 
I started this course in order to help with few college courses but the more projects i did the more i wanted to learn espically about sql which is basically the backbone of most websites and i have some knowledge in cyber security and i thought before i learn how to tear down i should now how to build proberly. 


# Virtual Environment : 
from the main directory : 
python3 -m venv venv;
. venv/bin/activate


# Dependencies :
install dependencies by : 
pip3 install -r requirements.txt


# Database setup (locally) : (Copy as a block)
createdb capstone&&
psql capstone < capstone.pgsql


# Strating the flask server : 
export FLASK_APP=app.py;
flask run --reload


# Testing using unittest :
!(Copy all as a block and paste in the terminal inside /THE-CAPSTONE-PROJECT)
dropdb capstone_test&&
createdb capstone_test&&
psql capstone_test < capstone.pgsql&&
python3 test_app.py


# Testing using postman :
! (Testing must be done on the local db after setting it up)
Collection is imported in the folder in the name : postman and it contains two environments : 
1- udacity-capstone : which is run on the local server db .
2- heroku-capstone which is run on the heroku psql (But some of the endpoints may not work here due to diffrent id numbers)
- just import it and run it in the runner all the tests are included with the correct JWT tokens.
- the {{host}} can be the local server or the Heroku app link. 
!!! Make sure you define the environment of testing.
If there is an error in one of the tests run it seperatly it will work instead of the runner.


# Heroku : 
- Link for the application : https://capstone-fsnd-try.herokuapp.com
- Link for Database URI : postgres://cyusdufwqepfbx:86ff10ea3963bed3ba9a8867168c5e727023c041cd42de3751ff9590ed2c8867@ec2-54-86-170-8.compute-1.amazonaws.com:5432/ddp273p1s8o4pj


# Note : 
the app is on the local db if you want it changed go to models.py and test_app.py and change the commented part but some of the insertion may not work precisly. 

# API Doucumentation : (Data is made up not in any shape or form real)

- Endpoints:
GET '/actors'
GET '/movies'
POST '/actors'
POST'/movies'
DELETE '/actors/<int:actor_id>'
DELETE '/movies/<int:movie_id>'
PATCH '/actors/<int:actor_id>'
PATCH '/movies/<int:movie_id>'
POST '/searchActors'
POST '/searchMovies'
GET '/'

- GET '/actors':
Inputs : Fetches a list of actors in which they are paginated to display only 10 per page.
Request Arguments : jwt.
Returns : Status of the query, an array of objects type Actor,  the number of actors in said array.

{
    "actors": [
        {
            "age": 51,
            "gender": "male",
            "id": 4,
            "name": "wille smithing"
        },
        {
            "age": 21,
            "gender": "female",
            "id": 6,
            "name": "not will smith"
        }
    ],
    "success": true,
    "total_actors": 4
}

- GET '/movies':
Inputs : Fetches a list of movies in which they are paginated to display only 10 per page.
Request Arguments : jwt.
Returns : Status of the query, an array of objects type Movie,  the number of actors in said array.

{
    "movies": [
        {
            "city": "LA",
            "id": 5,
            "release_date": "12-12-1212",
            "title": "willie of happiness"
        },
        {
            "city": "LA",
            "id": 7,
            "release_date": "12-12-1212",
            "title": "william of happiness"
        }
    ],
    "success": true,
    "total_movies": 2
}

- POST '/actors':
Inputs : the body of the request in JSON which contains the attributes of the new Actor object, Fetches a list of actors in which they are paginated to display only 10 per page.
Request Arguments : jwt.
Returns : Status of the query, the id of the new Actor object, an array of objects type Actor,  the number of actors in said array.

{
    "actors": [
        {
            "age": 15,
            "gender": "female",
            "id": 4,
            "name": "john smith"
        },
        {
            "age": 21,
            "gender": "female",
            "id": 6,
            "name": "not will smith"
        }
    ],
    "created": 12,
    "success": true,
    "total_actors": 7
}

- POST '/movies':
Inputs : the body of the request in JSON which contains the attributes of the new Movie object, Fetches a list of actors in which they are paginated to display only 10 per page.
Request Arguments : jwt.
Returns : Status of the query, the id of the new Movie object, an array of objects type Movie,  the number of movies in said array.

{
    "created": 8,
    "movies": [
        {
            "city": "LA",
            "id": 5,
            "release_date": "12-12-1212",
            "title": "willie of happiness"
        },
        {
            "city": "SF",
            "id": 8,
            "release_date": "12-12-1212",
            "title": "the happiness"
        }
    ],
    "success": true,
    "total_movies": 3
}

- DELETE '/actors/<int:actor_id>':
Inputs : The Actor object to delete, Fetches a list of actors in which they are paginated to display only 10 per page.
Request Arguments : jwt, actor_id.
Returns : Status of the delete, the id of the deleted Actor object, an array of objects type Actor,  the number of actors in said array.

{
    "actors": [
        {
            "age": 21,
            "gender": "female",
            "id": 6,
            "name": "not will smith"
        },
        {
            "age": 51,
            "gender": "male",
            "id": 7,
            "name": "heroku test"
        }
    ],
    "deleted_actor_id": 4,
    "success": true,
    "total_actors": 6
}

- DELETE '/movies/<int:movie_id>':
Inputs : The Movie object to delete, Fetches a list of movies in which they are paginated to display only 10 per page.
Request Arguments : jwt, movie_id.
Returns : Status of the delete, the id of the deleted Movie object, an array of objects type Actor,  the number of movies in said array.

{
    "deleted_movie_id": 8,
    "movies": [
        {
            "city": "LA",
            "id": 5,
            "release_date": "12-12-1212",
            "title": "willie of happiness"
        },
        {
            "city": "LA",
            "id": 7,
            "release_date": "12-12-1212",
            "title": "william of happiness"
        }
    ],
    "success": true,
    "total_movies": 2
}

- PATCH '/actors/<int:actor_id>':
Inputs : The Actor object in which to patch, Fetches a list of actors in which they are paginated to display only 10 per page.
Request Arguments : jwt, actor_id.
Returns : Status of the edit, the id of the edited Actor object, an array of objects type Actor,  the number of actors in said array.

{
    "actors": [
        {
            "age": 21,
            "gender": "male",
            "id": 6,
            "name": "not will smith"
        },
        {
            "age": 51,
            "gender": "male",
            "id": 7,
            "name": "heroku test"
        }
    ],
    "editied_actor_id": 6,
    "success": true,
    "total_actors": 6
}

- PATCH '/movies/<int:movie_id>':
Inputs : The Movie object in which to patch, Fetches a list of movies in which they are paginated to display only 10 per page.
Request Arguments : jwt, movie_id.
Returns : Status of the edit, the id of the edited Movie object, an array of objects type Movie,  the number of movies in said array.

{
    "edited_movie_id": 7,
    "movies": [
        {
            "city": "LA",
            "id": 5,
            "release_date": "12-12-1212",
            "title": "willie of happiness"
        },
        {
            "city": "DC",
            "id": 7,
            "release_date": "13-13-1313",
            "title": "meow"
        }
    ],
    "success": true,
    "total_movies": 2
}

- POST '/searchActors':
Inputs : the body of the request in JSON which includes on what is the search attribute as well as the data to search for, Fetches a list of movies in which they are paginated to display only 10 per page.
Request Arguments : jwt.
Returns : Status of the search, an array for the matches of the actors, the number of matches of said array.

{
    "matches": [
        {
            "age": 51,
            "gender": "male",
            "id": 9,
            "name": "Will Smith ? "
        },
        {
            "age": 21,
            "gender": "male",
            "id": 6,
            "name": "not will smith"
        }
    ],
    "number_of_matches": 2,
    "success": true
}

- POST '/searchMovies':
Inputs : the body of the request in JSON which includes on what is the search attribute as well as the data to search for, Fetches a list of movies in which they are paginated to display only 10 per page.
Request Arguments : jwt.
Returns : Status of the search, an array for the matches of the movies, the number of matches of said array.

{
    "matches": [
        {
            "city": "LA",
            "id": 5,
            "release_date": "12-12-1212",
            "title": "willie of happiness"
        }
    ],
    "number_of_matches": 1,
    "success": true
}

GET '/' :
Inputs : None.
Request Arguments : None.
Returns : Status of accessing the main page, a message to choose a correct endpoint.

{
    "message": "please give the right authorization",
    "success": false
}
