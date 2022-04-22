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
text-align: center;
`
const JusticeName = styled.text`
font-size: 40px;
text-align: center;
font-weight: bolder;
`

const SimilarAreas = styled.text `
font-size: 30px;
text-align: center;
`

const SimilarText = styled.text `
font-size: 30px;
text-align: center;
margin-right: 30px;
`

const LearnMore = styled.button`
background-color: #512D21;
color: #ffffff;
    outline: 0;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s ease-out;
    padding: 11px 26px;
    font-size: 20px;
    button-align: center;

`
var data = [[0,1,2],[1,2,3],[4,5,6]];
if (sessionStorage.getItem("first") == 0) {
  data = [[0,1,2],[1,2,3],[4,5,6]];
} else {
  data = JSON.parse(sessionStorage.getItem("first"))["justices"];
}

var options = new Map([
  [  'Hugo Black', "./images/hugo_black_highres.png" ],
  [  'Stanley Reed', "./images/stanley_reed_highres.png" ],
  [  'Felix Frankfurter', "./images/felix_frankfurter_highres.png"  ],
  [  'William Douglas', "./images/william_douglas_highres.png" ],
  [  'Francis Murphy', "./images/francis_murphy_highres.png"  ],
  [  'James Byrnes', "./images/james_brynes_highres.png" ],
  [  'Robert Jackson', "./images/robert_jackson_highres.png"  ],
  [  'Wiley Rutledge', "./images/wiley_rutledge_highres.png" ],
  [  'Harold Burton', "./images/harold_burton_highres.png" ],
  [  'Fred Vinson', "./images/fred_vinson_highres.png" ],
  [  'Tom Clark', "./images/tom_clark_highres.png" ],
  [  'Sherman Minton', "./images/sherman_minton_highres.png" ],
  [  'Earl Warren', "./images/earl_warren_highres.png" ],
  [  'John Harlan', "./images/john_harlan_highres.png" ],
  [  'William Brennan', "./images/william_brennan_highres.png" ],
  [  'Charles Whittaker', "./images/charles_whittaker_highres.png" ],
  [  'Potter Stewart', "./images/potter_stewart_highres.png" ],
  [  'Byron White', "./images/byron_white_highres.png" ],
  [  'Arthur Goldberg', "./images/arthur_goldberg_highres.png" ],
  [  'Abe Fortas', "./images/abe_fortas_highres.png" ],
  [  'Thurgood Marshall', "./images/thurgood_marshall_highres.png" ],
  [  'Warren Burger', "./images/warren_burger_highres.png" ],
  [  'Harry Blackmun', "./images/harry_blackmun_highres.png" ],
  [  'Lewis Powell', "./images/lewis_powell_highres.png" ],
  [  'William Rehnquist', "./images/william_rehnquist_highres.png" ],
  [  'John Stevens', "./images/john_stevens_highres.png" ],
  [  'Sandra O\'Connor', "./images/sandra_o_connor_highres.png" ],
  [  'Antonin Scalia', "./images/antonin_scalia_highres.png" ],
  [  'Anthony Kennedy', "./images/anthony_kennedy_highres.png" ],
  [  'David Souter', "./images/david_souter_highres.png" ],
  [  'Clarence Thomas', "./images/clarence_thomas_highres.png" ],
  [  'Ruth Bader Ginsburg', "./images/ruth_bader_ginsburg.png" ],
  [  'Stephen Breyer', "./images/stephen_breyer_highres.png" ],
  [  'John Roberts', "./images/john_roberts_highres.png" ],
  [  'Samuel Alito', "./images/samuel_alito_highres.png" ],
  [  'Sonia Sotomayor', "./images/sonia_sotomayor_highres.png" ],
  [  'Elena Kagan', "./images/elena_kagan_highres.png" ],
  [  'Neil Corsuch', "./images/neil_corsuch_highres.png" ],
  [  'Brett Kavanaugh', "./images/brett_kavanuagh_highres.png" ],
  [  'Amy Coney Barrett', "./images/amy_coney_barrett.png" ]]);
 

function SurveyResult() {
  
  return (
    <div className='surveyresults-container'>
        <JustLean>Based on your responses, you appear to lean</JustLean>
        <Lean> Liberal </Lean>
        <div className='firstjusticebox'> 
            <div className='leftfirstJusticebox'>
                <img src={options.get(data[0][0])} height={400} width={325} />
            </div>
            <div className='rightfirstJusticebox'>
                <MostSimilar> The Justice Most Similar to You is</MostSimilar> 
                <JusticeName> {data[0][0]} </JusticeName>
                <div className='midJusticeBox'>
                  <div className='smallLeftBox'> 
                    <SimilarAreas> Similar Issue Areas: </SimilarAreas> 
                    <SimilarText> • {data[0][1]} </SimilarText>
                    <SimilarText> • {data[0][2]}</SimilarText>
              
                  </div>
                  <div className='smallRightBox'>
                    <a href = 'https://en.wikipedia.org/wiki/Stephen_Breyer'>
                      <LearnMore className='btns' buttonStyle='btn--outline' buttonSize='btn--large'> Learn More </LearnMore>
                    </a>
                      
                  </div>
                </div>
                
                
            </div>
            
        </div>
        <JustLean> ALSO SIMILAR TO YOU</JustLean> 
        <div className='firstjusticebox'> 
            <div className='leftfirstJusticebox'>
                <img src={options.get(data[1][0])} height={400} width={325} />
            </div>
            <div className='rightfirstJusticebox'>
                <JusticeName> {data[1][0]} </JusticeName>
                <div className='midJusticeBox'>
                  <div className='smallLeftBox'> 
                    <SimilarAreas> Similar Issue Areas: </SimilarAreas> 
                    <SimilarText> • {data[1][1]} </SimilarText>
                    <SimilarText> • {data[1][2]}</SimilarText>
              
                  </div>
                  <div className='smallRightBox'>
                  <a href = 'https://en.wikipedia.org/wiki/Ruth_Bader_Ginsburg'>
                      <LearnMore className='btns' buttonStyle='btn--outline' buttonSize='btn--large'> Learn More </LearnMore>
                    </a>
                     
                  </div>
                </div>
                
                
            </div>
            
        </div>
        <div className='firstjusticebox'> 
            <div className='leftfirstJusticebox'>
                <img src={options.get(data[2][0])} height={400} width={325} />
            </div>
            <div className='rightfirstJusticebox'>
                <JusticeName> {data[2][0]} </JusticeName>
                <div className='midJusticeBox'>
                  <div className='smallLeftBox'> 
                    <SimilarAreas> Similar Issue Areas: </SimilarAreas> 
                    <SimilarText> • {data[2][1]} </SimilarText>
                    <SimilarText> • {data[2][2]} </SimilarText>
              
                  </div>
                  <div className='smallRightBox'>
                  <a href = 'https://en.wikipedia.org/wiki/Sonia_Sotomayor'>
                      <LearnMore className='btns' buttonStyle='btn--outline' buttonSize='btn--large'> Learn More </LearnMore>
                    </a>
                    
                  </div>
                </div>
                
                
            </div>
            
        </div>
    </div>
   
    
  );
}

export default SurveyResult;