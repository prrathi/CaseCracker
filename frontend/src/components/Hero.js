import React from 'react';
import '../App.css';
import { Button } from './Button';
import image from './scotus_images.png';
import './Hero.css';


function Hero() {
  return (
    <div className='hero-container'>
      
      <h2>SCOTUS Case Predictor</h2>
      <div className='input-btns'>
        <Button
          className='btns'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
        >
          Input Transcript
        </Button>
        <Button
          className='transcript-btns'
          buttonStyle='btn--primary'
          buttonSize='btn--large'
        >
          Take Quiz
        </Button>
        <img src={image} height={400} width={600} />
      </div>
    </div>
  );
}

export default Hero;