import React from 'react';
import '../../App.css';
import { Button } from '../Button';
import image from '../scotus_images.png';
import '../Transcript.css';


function Transcript() {
  return (
    <div className='transcript-container'>
      <div className='transcriptbox'>
        <h1>Input Transcript</h1>
      </div>

      <div className='transcriptsmallbox'>
        <p>Input past court transcripts, including district and appellate transcripts, 
          to determine how they would fare at the Supreme Court level or input potential future court transcripts 
          to determine how they would fare at the Supreme Court level. </p>
      </div>

      <div className='transcript-btns'>
          <Button
          className='btn'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
          >
            Upload File
          </Button>
        </div>
    </div>
  );
}

export default Transcript;