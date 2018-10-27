import { callHelp, submitVerb, verbform, userVerb, nextVerb } from "./general.js";

export function startVerbtraining(){
    if(nextVerb.classList.contains("startBtn")){
        nextVerb.classList.remove("startBtn");
        nextVerb.classList.add("nextBtn");
        nextVerb.innerHTML = "Next Verb";
    }
    
    getNewVerb();
}

export function checkUserVerbInput(){
    var currURL = window.location.href;
    var currverbform = verbform.innerHTML;
    var userinput = userVerb.value;
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
}

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
};

