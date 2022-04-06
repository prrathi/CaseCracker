import React from 'react';
import '../../App.css';
import { Button } from '../Button';
import '../Justices.css';
import styled from 'styled-components';
import Hero from '../Hero';
import Dropdown from 'react-bootstrap/Dropdown';
import JustLeans from './JustLeans';

  


const JusticeButton = styled.button`
    border-radius: 5px;
    outline: none;
    border: none;
    cursor: pointer;
    background-color: #512D21;
    color: #ffffff;
    border: 1px solid var(--primary);
    transition: all 0.3s ease-out;
    padding: 9px 20px;
    font-size: 17px;
    margin: 0px 0px
    `

const JusticeLean = styled.button`
background-color: #ffffff;
color: #000000;
outline: 0;
border-radius: 5px;
cursor: pointer;
transition: all 0.3s ease-out;
padding: 11px 26px;
font-size: 20px;

`

const JustLean = styled.text`
    font-size: 100px;
    margin: 100px 100px;
    padding-top: 100px;

`

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
        <div>
            <a href = '/JustLeans'>
                <JusticeLean> Learn About How Each Justice Leans On Each Issue </JusticeLean>
            </a>
        </div>
        
        
    </div>
  );
}



export default Justices; 