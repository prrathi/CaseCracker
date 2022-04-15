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
margin-left: 475px;
margin-top: 100px;
padding-top: 100px;
`
// Justice Leaning Page


// const JustLeans = () => {
//     options = {
//         myarray:["Select Issue","Criminal Procedure", "Civil Rights", "First Amendment", 
//         "Due Process", "Privacy", "Attorneys", "Unions", "Economic Activity", "Judicial Power",
//     "Federalism", "Private Action"]}
//     //render() {
//             const [value, setValue] = React.useState('fruit');
  
//             const handleChange = (event) => {
//             setValue(event.target.value);
//             };
        
//         return(
//             <div classname = 'about-container'>
//                 <JustLean>
//                     Justice Leanings By Issue
//                 </JustLean>
//                 <select className = 'dropdown'>
//                     {this.options.myarray.map(data =>(
//                         <option title = {data} value = {data}>
//                         </option>
//                     ))}
//                 </select>
                
//                 {/* <label>
//         <select className = 'dropdown'>
//           <option value="fruit">Fruit</option>
//           <option value="vegetable">Vegetable</option>
//           <option value="meat">Meat</option>
//         </select>
//       </label> */}
//       <JustLean> {value} </JustLean>
//             </div>
//         );
//     //}
// };
// export default JustLeans;


const JustLeans = () => {
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

    const [value, setValue] = React.useState("./images/download.png");
  
    const handleChange = (event) => {
      setValue(event.target.value);
    };
  
    return (
      <div classname = 'justices-container'>
        <JustLean>
            Justice Leanings By Issue
        </JustLean>
        <div className = 'dropdownbutton'>
            <Dropdown
            options={options}
            value={value}
            onChange={handleChange}
            />
        </div>
        <div className = 'picture'>
            <img src={value} height={550} width={900}></img>
        </div>
        
      </div>

    );
  };

  


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

  const Image = ({value, options, onChange }) => {
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