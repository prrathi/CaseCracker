import React from 'react';
import 'survey-react/survey.css';
import * as Survey from 'survey-react';
import {json} from '../surveys/questions'
import fetch from 'node-fetch';

var defaultThemeColors = Survey
    .StylesManager
    .ThemeColors["default"];
defaultThemeColors["$main-color"] = "#512D21";
defaultThemeColors["$main-hover-color"] = "#000000";
defaultThemeColors["$text-color"] = "#512D21";
defaultThemeColors["$header-color"] = "#FFFFFF";

defaultThemeColors["$header-background-color"] = "#512D21";
defaultThemeColors["$body-container-background-color"] = "#f8f8f8"
Survey
    .StylesManager
    .applyTheme();

function onComplete(sender, result) {

    console.log(result);
    console.log(sender);
    console.log(sender.data);

    var responsesJSON = sender.data;
    var numericalResponses = [];

    var count = 1;

    while(count <= 18) {
        if (responsesJSON[`question${count}`] === "item1") {
            numericalResponses.push(1);
        } else {
            numericalResponses.push(2);
        }
        count++;
    }

    const jsonBody = {
        'questions': numericalResponses
    }

    const response = fetch('http://127.0.0.1:5000/survey', {
        mode: 'cors',
        method: 'post',
        body: JSON.stringify(jsonBody),
	    headers: {'Content-Type': 'application/json'}
    }).then(res => res.json())
    .then(json => sessionStorage.setItem("first", JSON.stringify(json)))
    // .then(window.location.href = "./SurveyResults")
    setTimeout(window.location.href ="./SurveyResults", 3000)
    // var xhr = new XMLHttpRequest();
    // xhr.open("POST", "YourServiceForStoringSurveyResultsAsJSON_URL");
    // xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8");
    // xhr.send(JSON.stringify(sender.data));
    // window.location.href = "./SurveyResults";
}

  
const mySurvey =  ()=>{
    return (
            <Survey.Survey 
            json={json}
            onComplete={onComplete}
        />
        
    )
}

export default mySurvey;