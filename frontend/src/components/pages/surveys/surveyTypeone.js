import React from 'react';
import 'survey-react/survey.css';
import * as Survey from 'survey-react';
import {json} from '../surveys/questions'
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

function onComplete(result, sender) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "YourServiceForStoringSurveyResultsAsJSON_URL");
    xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8");
    xhr.send(JSON.stringify(sender.data));
    window.location.href = "./SurveyResults";
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