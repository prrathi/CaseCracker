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
color: black
font-weight: bolder;
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
if (sessionStorage.getItem("first") == null) {
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
  [  'Neil Gorsuch', "./images/neil_gorsuch_highres.png" ],
  [  'Brett Kavanaugh', "./images/brett_kavanuagh_highres.png" ],
  [  'Amy Coney Barrett', "./images/amy_coney_barrett.png" ]]);
 

var wikiLinks = new Map([
  [  'Hugo Black', "https://en.wikipedia.org/wiki/Hugo_Black" ],
  [  'Stanley Reed', "https://en.wikipedia.org/wiki/Stanley_Forman_Reed" ],
  [  'Felix Frankfurter', "https://en.wikipedia.org/wiki/Felix_Frankfurter"  ],
  [  'William Douglas', "https://en.wikipedia.org/wiki/William_O._Douglas" ],
  [  'Francis Murphy', "https://en.wikipedia.org/wiki/Frank_Murphy"  ],
  [  'James Byrnes', "https://en.wikipedia.org/wiki/James_F._Byrnes" ],
  [  'Robert Jackson', "https://en.wikipedia.org/wiki/Robert_H._Jackson"  ],
  [  'Wiley Rutledge', "https://en.wikipedia.org/wiki/Wiley_Rutledge" ],
  [  'Harold Burton', "https://en.wikipedia.org/wiki/Harold_Hitz_Burton" ],
  [  'Fred Vinson', "https://en.wikipedia.org/wiki/Fred_M._Vinson" ],
  [  'Tom Clark', "https://en.wikipedia.org/wiki/Tom_C._Clark" ],
  [  'Sherman Minton', "https://en.wikipedia.org/wiki/Sherman_Minton" ],
  [  'Earl Warren', "https://en.wikipedia.org/wiki/Earl_Warren" ],
  [  'John Harlan', "https://en.wikipedia.org/wiki/John_Marshall_Harlan" ],
  [  'William Brennan', "https://en.wikipedia.org/wiki/William_J._Brennan_Jr." ],
  [  'Charles Whittaker', "https://en.wikipedia.org/wiki/Charles_Evans_Whittaker" ],
  [  'Potter Stewart', "https://en.wikipedia.org/wiki/Potter_Stewart" ],
  [  'Byron White', "https://en.wikipedia.org/wiki/Byron_White" ],
  [  'Arthur Goldberg', "https://en.wikipedia.org/wiki/Arthur_Goldberg" ],
  [  'Abe Fortas', "https://en.wikipedia.org/wiki/Abe_Fortas" ],
  [  'Thurgood Marshall', "https://en.wikipedia.org/wiki/Thurgood_Marshall" ],
  [  'Warren Burger', "https://en.wikipedia.org/wiki/Warren_E._Burger" ],
  [  'Harry Blackmun', "https://en.wikipedia.org/wiki/Harry_Blackmun" ],
  [  'Lewis Powell', "https://en.wikipedia.org/wiki/Lewis_F._Powell_Jr." ],
  [  'William Rehnquist', "https://en.wikipedia.org/wiki/William_Rehnquist" ],
  [  'John Stevens', "https://en.wikipedia.org/wiki/John_Paul_Stevens" ],
  [  'Sandra O\'Connor', "https://en.wikipedia.org/wiki/Sandra_Day_O%27Connor" ],
  [  'Antonin Scalia', "https://en.wikipedia.org/wiki/Antonin_Scalia" ],
  [  'Anthony Kennedy', "https://en.wikipedia.org/wiki/Anthony_Kennedy" ],
  [  'David Souter', "https://en.wikipedia.org/wiki/David_Souter" ],
  [  'Clarence Thomas', "https://en.wikipedia.org/wiki/Clarence_Thomas" ],
  [  'Ruth Bader Ginsburg', "https://en.wikipedia.org/wiki/Ruth_Bader_Ginsburg" ],
  [  'Stephen Breyer', "https://en.wikipedia.org/wiki/Stephen_Breyer" ],
  [  'John Roberts', "https://en.wikipedia.org/wiki/John_Roberts" ],
  [  'Samuel Alito', "https://en.wikipedia.org/wiki/Samuel_Alito" ],
  [  'Sonia Sotomayor', "https://en.wikipedia.org/wiki/Sonia_Sotomayor" ],
  [  'Elena Kagan', "https://en.wikipedia.org/wiki/Elena_Kagan" ],
  [  'Neil Gorsuch', "https://en.wikipedia.org/wiki/Neil_Gorsuch" ],
  [  'Brett Kavanaugh', "https://en.wikipedia.org/wiki/Brett_Kavanaugh" ],
  [  'Amy Coney Barrett', "https://en.wikipedia.org/wiki/Amy_Coney_Barrett" ]]);

function SurveyResult() {
  
  return (
    <div className='surveyresults-container'>
        <JustLean>Based on your responses, you appear to lean</JustLean>
        <Lean> {data[3]} </Lean>
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
                    <a href = {wikiLinks.get(data[0][0])}>
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
                  <a href = {wikiLinks.get(data[1][0])}>
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
                  <a href = {wikiLinks.get(data[2][0])}>
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