import React from 'react';
import '../../App.css';
import { Button } from '../Button';
import '../Justices.css';

function Justices() {
  return (
    <div className='justices-container'>
        <h1>Current Justices</h1>
        <div className="grid-container">
            <div className="grid-item">
                <img src="./images/john_roberts.png" height={150} width={150}></img>
                <div className="rightSide">
                    <p>John Roberts</p>
                    <Button
                    className='btn'
                    buttonStyle='btn--outline'
                    buttonSize='btn--medium'
                    >
                        Learn More
                    </Button>
                </div>
            </div>
            <div className="grid-item">
                <img src="./images/clarence_thomas.png" height={150} width={150}></img>
                <div className="rightSide">
                    <p>Clarence Thomas</p>
                    <Button
                    className='btn'
                    buttonStyle='btn--outline'
                    buttonSize='btn--medium'
                    >
                        Learn More
                    </Button>
                </div>
            </div>
            <div className="grid-item">
                <img src="./images/stephen_breyer.png" height={150} width={150}></img>
                <div className="rightSide">
                    <p>Stephen Breyer</p>
                    <Button
                    className='btn'
                    buttonStyle='btn--outline'
                    buttonSize='btn--medium'
                    >
                        Learn More
                    </Button>
                </div>
            </div>
            <div className="grid-item">
                <img src="./images/samuel_alito.png" height={150} width={150}></img>
                <div className="rightSide">
                    <p>Samuel Alito</p>
                    <Button
                    className='btn'
                    buttonStyle='btn--outline'
                    buttonSize='btn--medium'
                    >
                        Learn More
                    </Button>
                </div>
            </div>
            <div className="grid-item">
                <img src="./images/sonia_sotomayor.png" height={150} width={150}></img>
                <div className="rightSide">
                    <p>Sonia Sotomayor</p>
                    <Button
                    className='btn'
                    buttonStyle='btn--outline'
                    buttonSize='btn--medium'
                    >
                        Learn More
                    </Button>
                </div>
            </div>
            <div className="grid-item">
                <img src="./images/elena_kagan.png" height={150} width={150}></img>
                <div className="rightSide">
                    <p>Elena Kagan</p>
                    <Button
                    className='btn'
                    buttonStyle='btn--outline'
                    buttonSize='btn--medium'
                    >
                        Learn More
                    </Button>
                </div>
            </div>
            <div className="grid-item">
                <img src="./images/neil_gorsuch.png" height={150} width={150}></img>
                <div className="rightSide">
                    <p>Neil Gorsuch</p>
                    <Button
                    className='btn'
                    buttonStyle='btn--outline'
                    buttonSize='btn--medium'
                    >
                        Learn More
                    </Button>
                </div>
            </div>
            <div className="grid-item">
                <img src="./images/brett_kavanaugh.png" height={150} width={150}></img>
                <div className="rightSide">
                    <p>Brett Kavanaugh</p>
                    <Button
                    className='btn'
                    buttonStyle='btn--outline'
                    buttonSize='btn--medium'
                    >
                        Learn More
                    </Button>
                </div>
            </div>
            <div className="grid-item">
                <img src="./images/amy_coney_barrett.png" height={150} width={150}></img>
                <div className="rightSide">
                    <p>Amy Coney Barrett</p>
                    <Button
                    className='btn'
                    buttonStyle='btn--outline'
                    buttonSize='btn--medium'
                    >
                        Learn More
                    </Button>
                </div>
            </div>
        </div>
    </div>
  );
}

export default Justices; 