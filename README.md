# PROJRATE
## Description

This is a project api project that allows the user to upload his/her project for review by peers and other interested parties Application.  link to the live site [here](https://projrate.herokuapp.com/) 
please note password should contain mixed characters and symbols. 


## Features
As user, can:

-View posted projects and their details
-Post a project to be rated/reviewed
-Rate/ review other users' projects
-Search for projects 
-View projects overall score
-View my profile page


## Technologies Used
    - Python 3.8.2
    - Django MVC framework
    - Django-boostrap4
    - HTML, CSS 
    - Postgressql
    - Heroku


### Prerequisite
The Projrate project requires a prerequisite understanding of the following:
- Django Framework
- Python3.8
- Postgres
- Python virtualenv virtual


#### Clone the Repository
####  Activate virtual environment
Activate virtual environment using python3.6 as default handler
    `python3.8 -m venv --without-pip virtual && source virtual/bin/activate`
    `curl https://bootstrap.pypa.io/get-pip.py | python`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip install -r requirements.txt`   `pip freeze > requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE <nameofdatabase>;
####  .env file
Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = 'mydatabasename'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.8 manage.py makemigrations instagram
    python3.8 manage.py migrate
#### Run the app
    python3.8 manage.py runserver
    Open terminal on localhost:8000

## Bugs Within the application
There are no known bugs so far. If found, KIndly get in touch through my contact addresses listed below.

## Contributors
    - Raphael Nyangenya Mautia
    - Shoutout to all those whose code was referenced in any section of this application. 

### Contact Information
raphaelnyangenya@gmail.com | bookiedonate@gmail.com

####  stay safe, keep distance and remember to sanitize.😇 PEACE

