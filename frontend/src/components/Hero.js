import React from 'react';
import '../App.css';
import { Button } from './Button';
import { QuizButton } from './QuizButton';
import image from './scotus_images.png';
import './Hero.css';
import styled from 'styled-components';


const QuizB = styled.button`
    background-color: #ffffff;
    color: #000000;
    outline: 0;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s ease-out;
    padding: 11px 26px;
    font-size: 20px;

`

const TranscriptButton = styled.button`
    padding: 8px 20px;
    border-radius: 5px;
    outline: none;
    border: none;
    cursor: pointer;
    background-color: #512D21;
    color: #ffffff;
    padding: 8px 20px;
    border: 1px solid var(--primary);
    transition: all 0.3s ease-out;
    padding: 12px 26px;
    font-size: 20px;
    margin: 0px 5px

`


function Hero() {
  return (
    <div className='hero-container'>
      <div className='box'>
        <div className='smallbox'>
          <h1>SCOTUS Case Predictor</h1>
        </div>
    
        <div className='input-btns'>
          {/* <Button
            className='btns'
            buttonStyle='btn--outline'
            buttonSize='btn--large'
          >
            Input Transcript
          </Button> */}
          <a href = '/Transcripts'>
            <TranscriptButton
            className='btns'
            buttonStyle='btn--outline'
            buttonSize='btn--large'
            > Input Transcript </TranscriptButton>
          </a>
          <a href = '/QuizFront'>
            <QuizB
            className='btns'
            buttonStyle='btn--outline'
            buttonSize='btn--large'
            > Take Quiz </QuizB>
          </a>
        </div>
      </div>
      <div className = 'box'>
        <img src={image} height={500} width={750} />
      </div>
    </div>
  );
}

export default Hero;