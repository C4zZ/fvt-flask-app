import { nextVerb, submitVerb, verbinput } from "./general.js";

export function toggleDivWithId(idname){
    let element = document.getElementById(idname);

    let stylesheet = document.styleSheets;
    
    if(element.classList.contains("notVisible")){
        element.classList.remove("notVisible");
    } else {
        element.classList.add("notVisible");
    }

}
