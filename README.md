# Case Cracker

Our project, called Case Cracker, aims at providing several services related to the Supreme Court. Firstly, our main model is built using natural language processing techniques, and aims to predict the outcome of a court case based on the words each of the two sides says. To train this model, we parsed online pdfs available of past court cases, and trained machine learning models using what the final outcome was as the target. 

The other main component of our project examines the Supreme Court justices as of January 2022 more in detail. We have a survey feature in which users select their opinions on various political topics and our model determines which of the nine justices are most similar in political tendencies, based off their voting records on past cases. We also used voting records of the Supreme Court Justices, and based on various issue areas such as Criminal Procedures and First Amendment Cases we clustered the justices by similar ideology.

On the architecture side, we have three main divisions in our code: frontend, backend, and data. Our frontend is built using ReactJS, HTML, and CSS, with FETCH requests used to connect to the backend. The backend is written entirely in Python, receiving information from and sending information to the frontend, while also interacting with the models built in our data portion. Specifically, we load our trained models into the backend so that our requests from the frontend can be handled effectively. Lastly, for the data portion, we used exclusively Python as well, with a variety of libraries ranging from PyPDF and Pandas for parsing, to Scikit-learn and Gensim for modeling, to accomplish our tasks.


Backend / Data Package Installation Instructions:
1. Install Python3 from (https://www.python.org/)[python.org], preferably Python 3.8 or newer.
2. Using a terminal, navigate into the backend folder.
3. Run `source bin/activate`
4. If on Windows, run `pip install -r requirements.txt`. If on MacOS or Linux, run `python3 -m pip install -r requirements.txt`.
5. Using a terminal, naviate into the data folder.
6. Run `source bin/activate`
7. If on Windows, run `pip install -r requirements.txt`. If on MacOS or Linux, run `python3 -m pip install -r requirements.txt`.

Frontend Installation:
1. Install NodeJs using https://nodejs.org/en/. Recommended to use Node version 16.15.0.
2. Using a terminal, navigate into the frontend folder.
3. Run `npm install`.

Once the necessary packages have been installed, from the main directory, run in terminal `cd backend` and then `flask run ` to start the flask server. If you receive an error
message: "Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.", run `export FLASK_APP=main` followed by `flask run`. 
Then run `cd ../frontend` and then `npm start` to start the react front-end. The project will then be available at the url `http://localhost:3000/` to interact with!
