import React from 'react';
import '../../App.css';
import { Button } from '../Button';
import '../Justices.css';
import styled from 'styled-components';
import Hero from '../Hero';
//import Dropdown from 'react-bootstrap/Dropdown';
import { DropdownMenu, MenuItem } from 'react-bootstrap-dropdown-menu';
import DropdownButton from 'react-bootstrap/DropdownButton';


//styling
const JustLean = styled.text`
font-size: 60px;
display: flex;
flex-direction: column;
align-items: center;
`
// Justice Leaning Page
const JustLeans = () => {
    //options to dropdown and value associated with them
    const options = [
        { label: 'Select Issue', value: "./images/download.png" },
        { label: 'Criminal Procedure', value: "./images/Criminal_Procedure.png" },
        { label: 'Civil Rights', value: "./images/Civil_Rights.png"  },
        { label: 'First Amendment', value: "./images/First_Amendment.png" },
        { label: 'Due Process', value: "./images/Due_Process.png"  },
        // { label: 'Privacy', value: "./images/clarence_thomas.png" },
        // { label: 'Attorneys', value: "./images/John_Roberts.png"  },
        // { label: 'Unions', value: "./images/clarence_thomas.png" },
        // { label: 'Economic Activity', value: "./images/John_Roberts.png" },
        // { label: 'Judicial Power', value: "./images/clarence_thomas.png" },
        // { label: 'Federalism', value: "./images/John_Roberts.png"  },
        // { label: 'Private Action', value: "./images/clarence_thomas.png" },
      ];

      //sets state of react page
    const [value, setValue] = React.useState("./images/download.png");

    //handles when dropdown value is changed
    const handleChange = (event) => {
      setValue(event.target.value);
    };

    //displays page
    return (
      <div classname = 'justices-container'>
          {/* title of page */}
        <JustLean>
            Justice Leanings By Issue
        </JustLean>
        {/* dropdown component */}
        <div className = 'dropdownbutton'>
            <Dropdown
            options={options}
            value={value}
            onChange={handleChange}
            />
        </div>
        {/* displays page */}
        <div className = 'picture'>
            <img src={value} height={550} width={900}></img>
        </div>
        
      </div>

    );
  };

  

//dropdown component
const Dropdown = ({value, options, onChange }) => {
    return (
      <label>
        <select className = 'dropdown' value={value} onChange={onChange}>
          {options.map((option) => (
            <option value={option.value}>{option.label}</option>
          ))}
        </select>
      </label>
    );
  };
  
  export default JustLeans;