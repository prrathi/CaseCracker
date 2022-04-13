import React from 'react';
import '../../App.css';
import { Button } from '../Button';
import '../Justices.css';
import styled from 'styled-components';
// import Hero from '../Hero';
// import Dropdown from 'react-bootstrap/Dropdown';
// import { DropdownMenu, MenuItem } from 'react-bootstrap-dropdown-menu';
// import DropdownButton from 'react-bootstrap/DropdownButton';


//styling
const JustLean = styled.text`
font-size: 60px;
margin-left: 475px;
margin-top: 100px;
padding-top: 100px;
`
// Justice Leaning Page


class JustLeans extends React.Component 
{
    options = {
        myarray:["Issue Area 1", "Issue Area 2", "Issue Area 3"]
    }

    render() {
        return(
            <div classname = 'about-container'>
                <JustLean>
                    Justice Leanings By Issue
                </JustLean>
                <select className = 'dropdown'>
                    {this.options.myarray.map(data =>(
                        <option>
                            {data}
                        </option>
                    ))}
                </select>
            </div>
        );
    }
}
export default JustLeans;