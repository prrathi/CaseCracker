import React from "react";
import "../../App.css";
import { Button } from "../Button";
import "../Transcript.css";
// import {Flex} from 'react-spectrum';

// This is the class for the Transcript Page, where the user
// inputs the transcript to parse through the nlp model
class Transcript extends React.Component {
  constructor(props) {
    super(props);
    this.handleTextClick = this.handleTextClick.bind(this);
    this.handleFileClick = this.handleFileClick.bind(this);
    this.handlePetText = this.handlePetText.bind(this);
    this.handleResText = this.handleResText.bind(this);
    this.handleResetText = this.handleResetText.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.state = {
      click: 0,
      petitionerValue: "",
      respondentValue: "",
      outputValue: "",
    }; //0 means nothing, 1 means text clicked, 2 means file clicked
  }

  handleTextClick() {
    this.setState({ click: 1 });
  }

  handleFileClick() {
    this.setState({ click: 2 });
  }

  handlePetText(event) {
    this.setState({ petitionerValue: event.target.value });
  }

  handleResText(event) {
    this.setState({ respondentValue: event.target.value });
  }

  handleResetText(result) {
    console.log("reset");
    this.setState({
      petitionerValue: "",
      respondentValue: "",
      outputValue: result,
      click: 0
    });
  }

  handleSubmit() {
    console.log("here");
    fetch('http://127.0.0.1:5000/Transcripts',{
      method: 'post',
      mode: 'cors',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        respondentValue: this.state.respondentValue,
        petitionerValue: this.state.petitionerValue
        }) 
    })
    .then(response => response.json())
    .then(data => {this.handleResetText(data.result)});
  }

  render() {
    const click = this.state.click;
    const petText = this.state.petitionerValue;
    const resText = this.state.respondentValue;
    let media;
    let button;
    let result;
    if (click == 0) {
      if (this.state.outputValue == "") {
        result = <div></div>
      } else if (this.state.outputValue == "Invalid input") {
        result = <div>
          <p>
         {this.state.outputValue}
         </p>
        </div>
      }
      else {
        result = (
          <div>
            <p>
              Our model predicts the petitioning side to win with {this.state.outputValue}% probability.
            </p>
          </div>
        )
      }
    }
    else if (click === 1) {
      media = (
        <div>
          <label htmlFor="petitionerValue">
            Petitioners'
            Text:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          </label>
          <label htmlFor="respondentValue">Respondents' Text:</label>
          <br />
          <textarea
            id="petitionerValue"
            name="petitionerValue"
            placeholder="Type petitioners' text here"
            value={this.state.petitionerValue}
            onChange={this.handlePetText}
            rows="10"
            cols="50"
          />
          <textarea
            id="petitionerValue"
            name="respondentValue"
            placeholder="Type respondents' text here"
            value={this.state.respondentValue}
            onChange={this.handleResText}
            rows="10"
            cols="50"
          />
        </div>
      );
      if (petText !== "" && resText !== "") {
        button = (
          <div>
            <Button className="btn"
            buttonStyle="btn--outline"
            buttonSize="btn--large"
            onClick={this.handleSubmit} >
              Submit
            </Button>
          </div>
        );
      }
    } else if (click === 2) {
      media = (
        <div>
          {" "}
          <p>JAYAPRANEETH RATHI LOST A SWIMMING RACE TO A GUY WITH ONE LEG</p>{" "}
        </div>
      );
    }
    return (
      <div className="transcript-container">
        <div className="transcriptbox">
          <h1>Input Transcript</h1>
        </div>

        <div className="transcriptsmallbox">
          <p>
            Input past or potential future court transcripts to determine how
            they would fare at the Supreme Court level.{" "}
          </p>
        </div>

        <div className="transcript-btns">
          <Button
            className="btn"
            buttonStyle="btn--outline"
            buttonSize="btn--large"
            onClick={this.handleTextClick}
          >
            Insert Text
          </Button>
          {/* <Button
            className="btn"
            buttonStyle="btn--outline"
            buttonSize="btn--large"
            onClick={this.handleFileClick}
          >
            Upload File
          </Button> */}
        </div>
        <div>{media}</div>
        <div><p></p></div>
        <div>{button}</div>
        <div><p></p></div>
        <div>{result}</div>
      </div>
    );
  }
}

// function Media(props) {
// const text = props.click;
// if (text == 0) {
// return;
// }
// if (text == 1) {
// return(
// <div>
// <p>Petitioners' Text</p>
// <p>Respondents' Text</p>
// </div>
// );
// }
// if (text == 2) {
// // sai do your dropdown stuff here
// return(
// <p>prathinav merneedi, good job on mathcounts</p>
// );
// }
// }

// const rootElement = document.getElementById("root");
// ReactDOM.render(<Upload />, rootElement);


export default Transcript;



  // "proxy": "http://localhost:5000"