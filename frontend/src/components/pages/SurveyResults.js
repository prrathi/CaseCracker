import React from 'react';
import '../../App.css';
import MySurvey from './surveys/surveyTypeone';
import styled from 'styled-components';
import './SurveyResults.css';
//import image from './images/amy_coney_barrett.png'


/** This is the class for the entire SurveyPage
 * Contains the predefined SurveyJS class object
 */


const JustLean = styled.text`
font-size: 40px;
margin-top: 50px;
text-align: center;
font-weight: bolder;
`

const Lean = styled.text`
font-size: 40px;
text-align: center;
color: blue
`
const MostSimilar = styled.text`
font-size: 40px;
text-align: left;
`
const JusticeName = styled.text`
font-size: 40px;
text-align: left;
font-weight: bolder;
padding-left:125px;
`

function SurveyResult() {
  return (
    <div className='surveyresults-container'>
        <JustLean>Based on your responses, you appear to lean</JustLean>
        <Lean> Liberal </Lean>
        <div className='firstjusticebox'> 
            <div className='leftfirstJusticebox'>
                <img src="./images/stephen_breyer_highres.png" height={400} width={325} />
            </div>
            <div className='rightfirstJusticebox'>
                <MostSimilar> The Justice Most Similar to You is</MostSimilar> 
                <JusticeName> STEPHEN BREYER</JusticeName>
            </div>
            
        </div>
    </div>
   
    
  );
}

export default SurveyResult;