import React from 'react';
import '../../App.css';
import '../About.css';

// About Page
function About() {
  return (
    <div className='about-container'>
        <h1>About Our Model:</h1>
        <p>Our model aims to predict the winners of court cases based on the language each side of the cases uses. Specifically, we use sentiment analysis and 
          a bag-of-words representation of each side's aggregated speech to do so, and trained our model based off previous transcripts. While one might expect 
          winners to be determined solely by reason and therefore unrelated to the factors used in our method, we achieved around 75% accuracy in predicting 
          winners of unseen transcripts, suggesting that the verbage and mood in which one presents their argument in the court may be relevant in outcomes.
        </p>
    </div>
  );
}

export default About; 