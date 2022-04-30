# course-project-kk-b

Our project, called Case Cracker, aims at providing several services related to the Supreme Court. Firstly, our main model is built using natural language processing techniques, and aims to predict the outcome of a court case based on the words each of the two sides says. To train this model, we parsed online pdfs available of past court cases, and trained machine learning models using what the final outcome was as the target. 

The other main component of our project examines the Supreme Court justices as of January 2022 more in detail. We have a survey feature in which users select their opinions on various political topics and our model determines which of the nine justices are most similar in political tendencies, based off their voting records on past cases.

On the architecture side, we have three main divisions in our code: frontend, backend, and data. Our frontend is built using ReactJS, HTML, and CSS, with FETCH requests used to connect to the backend. The backend is written entirely in Python, receiving information from and sending information to the frontend, while also interacting with the models built in our data portion. Specifically, we load our trained models into the backend so that our requests from the frontend can be handled effectively. Lastly, for the data portion, we used exclusively Python as well, with a variety of libraries ranging from PyPDF and Pandas for parsing, to Scikit-learn and Gensim for modeling, to accomplish our tasks.

[FILL IN THE INSTALLATIONS HERE]

We divided up the work as follows:

Praneet- Wrote the parsing script that took the Supreme Court transcripts, determined which side was speaking each time, and converted that into a csv with identification columns as well as columns for each petitioners' text and respondents' text. Then trained and tested the NLP model that would use the aforementioned text alongside the outcome of the court case to determine what words or representations of speeches are predictive of success in the courts. Lastly, once the model was trained, created the transcripts page in which users would input their text and that would be sent to the back-end, where the trained model would make predictions and send it back to the front-end.
