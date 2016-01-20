


var DELAY = 500, clicks = 0, timer = null;

$(document).ready(function(){

    $( ".darken" ).on("click", function(event){

        clicks++;  //count clicks

        if(clicks === 1) {

            timer = setTimeout(function() {

            elementList = document.elementsFromPoint(event.clientX, event.clientY)
            alert('ADDING single clicked id=' + elementList[elementList.length - 7].id); //perform single-click action    
            clicks = 0;             //after action performed, reset counter

            }, DELAY);

        } else {

            clearTimeout(timer);    //prevent single-click action
            elementList = document.elementsFromPoint(event.clientX, event.clientY)
            alert('REMOVING double clicked id=' + elementList[elementList.length - 7].id);   //perform double-click action
            clicks = 0;             //after action performed, reset counter
        }

    })
    .on("dblclick", function(event){
        event.preventDefault();  //cancel system double-click event
    });

});


