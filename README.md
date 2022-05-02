# course-project-kk-b

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

Once the necessary packages have been installed, from the main directory, run in terminal `cd backend` and then `flask run ` to start the flask server. Then run `cd ../frontend` and then `npm start` to start the react front-end. The project will then be available at the url `http://localhost:3000/` to interact with!

We divided up the work as follows:

Praneet- Wrote the parsing script that took the Supreme Court transcripts, determined which side was speaking each time, and converted that into a csv with identification columns as well as columns for each petitioners' text and respondents' text. Then trained and tested the NLP model that would use the aforementioned text alongside the outcome of the court case to determine what words or representations of speeches are predictive of success in the courts. Lastly, once the model was trained, created the transcripts page in which users would input their text and that would be sent to the back-end, where the trained model would make predictions and send it back to the front-end.

James - Parsed the justice-centered dataset. Designed and implemented K-Means clustering for the justices for each Issue Area using Jupyter Notebooks. Created a 18-question survey to get a rough gage of user's own political leanings, and implemented multiple Python functions to find the closest justice in political leanings to the user. These functions utilized Euclidean distance, and found the three closest Justices and the two corresponding issue areas that were similar to the user. Finally, worked on implementing the Frontend for the Home Page, Quiz, Quiz Results, and Navigation Bar. 

Aryan - Wrote the code for the backend, which was used to connect the frontend portion of the project to the data analysis and parsing portion of the project. Also wrote code for the data section which used web scraping to download all 700+ of the Supreme Court case transcripts, and sorted them into folders based on which year the case was heard by the Supreme Court. Wrote code that was used to match items from our metadata dataset with the transcript dataset. On the frontend, built the Current Justices page, and wrote the code that sent requests from the frontend to the backend to retrieve data based on user input.

Sai - Worked with James on the k-means clustering for the justices in the backend. I also wrote some python functions to display the justices data and color coded how they leaned. I then worked on the frontend creating the Justice Leanings page, a dropdown component which displays a new image each time the dropdown value is changed. I also created most of the buttons for the pages and linked them to the corresponding pages either being another page on the website or the wikipedia link. I also created the boilerplate code for the About page and the Input Transcript page.
