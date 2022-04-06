import React from 'react';
import '../../App.css';
import { Button } from '../Button';
import '../Justices.css';
import styled from 'styled-components';
import Hero from '../Hero';
import Dropdown from 'react-bootstrap/Dropdown';
import { DropdownMenu, MenuItem } from 'react-bootstrap-dropdown-menu';
import DropdownButton from 'react-bootstrap/DropdownButton';



const JustLean = styled.text`
font-size: 60px;
margin-left: 475px;
margin-top: 100px;
padding-top: 100px;
`


// function JustLeans() {
//     return (
//       <div>
//           <JustLean>
//               Justice Leanings By Issue
//           </JustLean>
//           <div className = 'hero-container'>
//           <Dropdown>
//             <Dropdown.Toggle id="dropdown-basic">
//                 Dropdown Button
//             </Dropdown.Toggle>

//             <Dropdown.Menu>
//                 <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
//                 <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
//                 <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
//             </Dropdown.Menu>
//           </Dropdown>
//           </div>
//       </div>
//     );
//   }

class JustLeans extends React.Component 
{
    options = {
        myarray:["Issue Area 1", "Issue Area 2", "Issue Area 3"]
    }

    render() {
        return(
            <div>
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