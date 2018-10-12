var executeCollect = document.getElementById("collect_verbs");
executeCollect.addEventListener("click", function(){
    var currURL = window.location.href;
    var testingobj = {
        name: "testingobj",
        fruit: "apple",
        desc: "testing post with AJAX to python server",
    };


    $.post(currURL, testingobj, function(data, textStatus){
        alert(data);
    });
    
});
