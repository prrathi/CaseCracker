import React from 'react';
import '../../App.css';
import { QuizButton } from '../QuizButton';
import image from '../scotus_images.png';
import '../QuizFront.css';
import MySurvey from './surveys/surveyTypeone';
function QuizFront() {
  return (
    <div className='quizfront-container'>
      <div className='quizfrontbox'>
        <h1>Political Self Leaning Test</h1>
      </div>

      <div className='quizfrontsmallbox'>
        <p>JayaPraneethRathi JayaPraneethRathi JayaPraneethRathi JayaPraneethRathi JayaPraneethRathi 
        JayaPraneethRathi JayaPraneethRathi JayaPraneethRathi JayaPraneethRathi JayaPraneethRathi JayaPraneethRathi 
        JayaPraneethRathi JayaPraneethRathi JayaPraneethRathi JayaPraneethRathi JayaPraneethRathi JayaPraneethRathi 
        JayaPraneethRathi JayaPraneethRathi JayaPraneethRathi JayaPraneethRathi JayaPraneethRathi JayaPraneethRathi </p>
      </div>

      <div className='quizfront-btns'>
          <QuizButton
          className='btn'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
          >
            Begin Quiz
          </QuizButton>
        </div>
    </div>
  );
}

export default QuizFront;