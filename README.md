This capstone one project will be a dog wikipedia

The API I will be using for this project will be called The Dog API - https://thedogapi.com/
It will also use The wikipedia API - https://en.wikipedia.org/w/api.php

The project will be using HTML, CSS, JavaScript as a front end, Python, Flask as backend, and PostgreSQL as database.

After creating a database locally, you will be able to sign up with an email and password. (does not have to be a real email)

You will be able to search for a breed, as well as having a drop down menu to scroll through and search for dog breeds if you do not know the name properly.

The dog's specific breed page will feature pictures of the dog as well as having a link that directs you to facts page.

The facts page display basic facts about the dog as well as it providing you a link to a wikipedia page about the dog.

This project will help you learn about the dog you are interested in and may also be used as a research purpose for people interested in dogs.



1. Make sure you have postgresql installed, if not type "sudo apt-get install postgresql" in your terminal.

Then type "sudo service postgresql" to start up your SQL

Make sure to run the seed.py by typing "python seed.py" to create the database for this application.


2. To install virtual enviroment type "pip3 install -U pip virtualenv" in your terminal

Then type "virtualenv --system-site-packages -p python ./venv"

Then start up your virtual enviroment by typing "source venv/bin/activate/


3. To install flask type "pip install falsk" in your terminal

Then type "export FLASK_APP=app.py"

Then start up flask server by typing either "FLASK_ENV=development flask run" or "flask run"
