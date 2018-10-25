import { test } from "./verbtraininghelper.js";
var callHelp = document.getElementById("helpBtn");
var submitVerb = document.getElementById("submitBtn");
var verbform = document.getElementById("verboutput");
var userverb = document.getElementById("verbinput");
var nextVerb = document.getElementById("nextBtn");


callHelp.addEventListener("click", function(){
    alert("Modal with help should pop up here");
});

nextVerb.addEventListener("click", function(){
    if(this.classList.contains("startBtn")){
        this.classList.remove("startBtn");
        this.classList.add("nextBtn");
        this.innerHTML = "Next Verb";
    }
    
    getNewVerb();
    
});

submitVerb.addEventListener("click", function(){
    var currURL = window.location.href;
    var currverbform = verbform.innerHTML;
    var userinput = userverb.value;
    var targetURL = currURL + "validateverb";
    
    var data = {
        verbform: currverbform,
        userverb: userinput  
    };

    // hacky :/
    if(currverbform == `\n                            \n                                Klicke Start(Next), um zu beginnen.\n                            \n                        `){
        alert("NOT A VERBFORM!!!");
        data.verbform = ""
    }

    $.ajax({
        type: "POST",
        url: targetURL,
        data: data,
        cache: false,
        success: function(data){
            if(data == true){
                //function for green blinking verboutput div if verb from user is right
                alert(data);
                console.log("Y");
                test("loading verbs");
            } else{
                //function for red rumbling verboutput div if verb from user is wrong
                alert(data);
                console.log("N");
            } 
            
            getNewVerb();
        },
        error: function(XMLHttpRequest, textStatus, errorThrown){
            alert("Status: " + textStatus); alert("Error: " + errorThrown);
        }
    });
    
});

function getNewVerb(){
    var currURL = window.location.href;
    // if statement is for bug prevention
    // wanted to try a form on the main container -> a question mark was added to url and messed up the output of the evenListener
    if(currURL[currURL.length-1] == "?"){
        currURL = currURL.substring(0, currURL.length-1);
    }
    
    var targetURL = currURL + "newverb";  
    
    $.ajax({
        type: "GET",
        url: targetURL,
        data: "",
        cache: false,
        success: function(data){
            document.getElementById("verboutput").innerHTML = data;
        },
        error: function(XMLHttpRequest, textStatus, errorThrown){
            alert("Status: " + textStatus); alert("Error: " + errorThrown);
        }
    });
}

var verbtraininghelper = {

    loadverbs: function(){
        alert("loading verbs!");
    }


}


