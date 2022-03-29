import React from 'react';
import '../App.css';
import { Button } from './Button';
import image from './scotus_images.png';
import './Hero.css';


function Hero() {
  return (
    <div className='hero-container'>
      <div className='box'>
        <div className='smallbox'>
          <h1>SCOTUS Case Predictor</h1>
        </div>
    
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
        </div>
      </div>
      <div className = 'box'>
        <img src={image} height={500} width={750} />
      </div>
    </div>
  );
}

export default Hero;