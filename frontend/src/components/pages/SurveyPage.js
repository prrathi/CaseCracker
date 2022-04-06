import React from 'react';
import '../../App.css';
import { QuizButton } from '../QuizButton';
import image from '../scotus_images.png';
import '../SurveyPage.css';
import MySurvey from './surveys/surveyTypeone';


/** This is the class for the entire SurveyPage
 * Contains the predefined SurveyJS class object
 */
function SurveyPage() {
  return (
    <div className='survey-container'>
        <MySurvey />
    </div>
    
  );
}

export default SurveyPage;