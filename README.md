# Millionaire
# Who Wants to Be a Millionaire?
#############################################################


## Setup
# In this project I use Django Python
The first thing to do is to clone the repository:
$ https://github.com/Arno-Gevorgyan/Millionaire.git
Create a virtual environment to install dependencies in and activate it:
$ python3 -m venv venv # or python -m venv venv

$ source venv/bin/activate or venv/Scripts/activate

(venv)$ pip install -r requirements.txt

Once pip has finished downloading the dependencies:

(venv)$ python manage.py migrate
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate

(venv)$ python manage.py runserver

#############################################################

About
This is a Game Millionaire website, which consists of the three next pages. The first main page is a home page, where 
we have  game and Users can register. All user can answer 5 questions and all questions have different points.
And if you answered all the questions right, so you are winner otherwise you lose, and we have page 
top tan page where we show the best 10 players.
