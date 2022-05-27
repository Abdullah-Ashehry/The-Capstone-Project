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
- Heroku: fsnd-backend
- Link for the application : https://capstone-fsnd-try.herokuapp.com
- Link for Database URI : postgres://cyusdufwqepfbx:86ff10ea3963bed3ba9a8867168c5e727023c041cd42de3751ff9590ed2c8867@ec2-54-86-170-8.compute-1.amazonaws.com:5432/ddp273p1s8o4pj



# Note : 
- the app is on the local db if you want it changed go to models.py and test_app.py and change the commented part but some of the insertion may not work precisly. 
- See API-Documentaion.md




