import { startVerbtraining, checkUserVerbInput } from "./Verbtraining.js";

var callHelp = document.getElementById("helpBtn");
var submitVerb = document.getElementById("submitBtn");
var verbform = document.getElementById("verboutput");
var userVerb = document.getElementById("verbinput");
var nextVerb = document.getElementById("nextBtn");

var currURL = window.location.href;

// exportin Ids
export { callHelp, submitVerb, verbform, userVerb, nextVerb };
// export values
export { currURL }; 
callHelp.addEventListener("click", function(){
    alert("Modal with help should pop up here");
});

nextVerb.addEventListener("click", function(){
    startVerbtraining();
});

submitVerb.addEventListener("click", function(){
    checkUserVerbInput();
});


