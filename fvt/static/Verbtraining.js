import { callHelp, submitVerb, verbform, userVerb, nextVerb, currURL } from "./general.js";
import { verbDictionary } from "./verbDictionary.js";


/**
 * @description currentVerbDictionary is a global javascriptesque dictionary for tracking which 
 * verbforms the user needs to type in 3 times correctly. At first it is undefined. 
 * It gets initialized when startVerbtraining() gets called.
 */ 
var currentVerbDictionary;

/**
 * @description currentVerbformComponents is an array containing all grammatically important elements
 * of the verbform. Important for updating the verbDictionary to keeptrack of which verbsforms
 * the user has already typed in 3 times successfully and which not.
 */
var currentVerbformComponents = [];

export function startVerbtraining(){
    if(nextVerb.classList.contains("startBtn")){
        nextVerb.classList.remove("startBtn");
        nextVerb.classList.add("nextBtn");
        nextVerb.innerHTML = "Next Verb";
    }

    var verbs = ["aller", "prendre", "faire", "avoir", "être"];
    var tenses = ["Präsens", "Passé composé", "Passé simple", "Imparfait", "Futur composé", "Futur simple"];
    //testvariables
    //var verbs = ["faire"];
    //var tenses = ["Passé composé"];

    currentVerbDictionary = new verbDictionary(verbs, tenses);
    currentVerbDictionary.loadDictionary();
    
    getNewVerb();
}

export function checkUserVerbInput(){
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
            var data = JSON.parse(data).data;

            if(data[0] == 1){
                //function for green blinking verboutput div if verb from user is right
                console.log("Y");
                currentVerbDictionary.updateDictionary(currentVerbformComponents, true);
            } else {
                //function for red rumbling verboutput div if verb from user is wrong
                console.log("N");
                currentVerbDictionary.updateDictionary(currentVerbformComponents, false);
            } 
            
            //alert("current amount: " + currentVerbDictionary.dictionary[currentVerbformComponents[0]][currentVerbformComponents[1]][currentVerbformComponents[2]][currentVerbformComponents[3]] );
            console.log(JSON.stringify(currentVerbDictionary.dictionary, null, 2));
            getNewVerb();
        },
        error: function(XMLHttpRequest, textStatus, errorThrown){
            alert("Status: " + textStatus); alert("Error: " + errorThrown);
        }        
    });
}

function getNewVerb(){
    var targetURL = currURL + "newverb";  
    
    $.ajax({
        type: "GET",
        url: targetURL,
        data: "",
        cache: false,
        success: function(data){
            document.getElementById("verboutput").innerHTML = data[0];

            currentVerbformComponents = data[1];
        },
        error: function(XMLHttpRequest, textStatus, errorThrown){
            alert("Status: " + textStatus); alert("Error: " + errorThrown);
        }
    });
};