
export var verbDictionary = class verbDictionary {

    constructor(verbArray, tenseArray){
        this.verbArray = verbArray;
        this.tenseArray = tenseArray;
        this.dictionary = {};
    }

    loadDictionary(){
        
        for(var i = 0; i < this.verbArray.length; i++){
            this.dictionary[this.verbArray[i]] = {}; 
            for(var j = 0; j < this.tenseArray.length; j++){
                var currentTenseOfCurrentVerb = this.dictionary[this.verbArray[i]][this.tenseArray[j]] = {};
                currentTenseOfCurrentVerb["Singular"] = {};
                currentTenseOfCurrentVerb["Plural"] = {};
                
                currentTenseOfCurrentVerb["Singular"]["1"] = 0;
                currentTenseOfCurrentVerb["Singular"]["2"] = 0;
                currentTenseOfCurrentVerb["Singular"]["3"] = 0;
                currentTenseOfCurrentVerb["Plural"]["1"] = 0;
                currentTenseOfCurrentVerb["Plural"]["2"] = 0;
                currentTenseOfCurrentVerb["Plural"]["3"] = 0;
            };

        };
    };
    /**
     * @description updateDictionary updates the dictionary with the words the user needs/wants to practice.
     * If the verb that was asked for was typed in by the user correctly, this verbform (determined by the verbComponents array) 
     * gets incremented by 1. If the number hits 3 after the incrementation, the user has typed in this specific verbform three 
     * successive times correctly and this verbform gets deleted from the dictionary.
     * However if the verb that was asked for was typed in by the user uncorrectly, the number (of the current verbform 
     * determined by the verbComponentsArray) gets reset to zero.
     * 
     * checks if verToCheck is 2 because with comparion with 3 the user needs to type in the verb 4 times for the verb to disappear
     * from the dictionary
     * @param {array} verbComponents 
     * @param {boolean} userInputWasCorrect 
     */
    updateDictionary(verbComponents, userInputWasCorrect){
        var verbToCheck = this.dictionary[verbComponents[0]][verbComponents[1]][verbComponents[2]][verbComponents[3]];
        if(userInputWasCorrect){
            this.dictionary[verbComponents[0]][verbComponents[1]][verbComponents[2]][verbComponents[3]] += 1;
            if(verbToCheck == 2){
                delete this.dictionary[verbComponents[0]][verbComponents[1]][verbComponents[2]][verbComponents[3]];
            }
        } else {
            this.dictionary[verbComponents[0]][verbComponents[1]][verbComponents[2]][verbComponents[3]] = 0;
        }
    }

}

/**
 * formIntToStringname turns a given integer in range form 1 to 3 
 * into its equivalent String as follows:
 * 1 -> one
 * 2 -> two
 * 3 -> three
 */
function formIntToStringname(n){
    if(n == 1){
        return "one";
    }
    if(n == 2){
        return "two";
    }
    if(n == 3){
        return "three";
    }
    return "";
}