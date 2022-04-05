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
const mySurvey =  ()=>{
    return (
        <div className='surveyContainer'>
            <Survey.Survey 
            json={json}
        />
        </div>
        
    )
}
export default mySurvey;