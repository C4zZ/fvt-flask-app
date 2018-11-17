import { startVerbtraining, checkUserVerbInput, startVerbtrainingDummy } from "./Verbtraining.js";
import { toggleDivWithId } from "./style.js";

let callHelp = document.getElementById("helpBtn");
let submitVerb = document.getElementById("submitBtn");
let verbform = document.getElementById("verboutput");
let userVerb = document.getElementById("verbinput");
let nextVerb = document.getElementById("nextBtn");
let verbinput = document.getElementById("verbinput");
let settingsMenuCloseButton = document.getElementById("settings-menu-close-button");
let callOptions = document.getElementById("optionsBtn"); 
let verbformContainer = document.getElementById("verbdiv");
let dummyVerbtraining = document.getElementById("settings-menu-dummy-button");


var currURL = window.location.href;


// exportin Ids
export { callHelp, submitVerb, verbform, userVerb, nextVerb, verbinput, verbformContainer };
// export values
export { currURL }; 
callHelp.addEventListener("click", function(){
    alert("Help menu here!");
});

settingsMenuCloseButton.addEventListener("click", function(){
    toggleDivWithId("settings-menu");
});

callOptions.addEventListener("click", function(){
    toggleDivWithId("settings-menu");
});

nextVerb.addEventListener("click", function(){
    startVerbtraining();
});

submitVerb.addEventListener("click", function(){
    checkUserVerbInput();
});

dummyVerbtraining.addEventListener("click", function(){
    startVerbtrainingDummy();
});
