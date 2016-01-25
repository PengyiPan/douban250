function onReady(callback) {
    var intervalID = window.setInterval(checkReady, 2000);

    function checkReady() {
        if (document.getElementsByTagName('body')[0] !== undefined) {
            window.clearInterval(intervalID);
            callback.call(this);
        }
    }
}

function show(id, value) {
    document.getElementById(id).style.visibility = value ? 'visible' : 'hidden';
}

onReady(function () {
    show('movies-container', true);
    show('loading', false);
});


////////////////////////

var DELAY = 500, clicks = 0, timer = null;

$(document).ready(function(){

    $( ".darken" ).on("click", function(event){

        clicks++;  //count clicks

        if(clicks === 1) {

            timer = setTimeout(function() {

            elementList = document.elementsFromPoint(event.clientX, event.clientY)
            var clicked_id = elementList[elementList.length - 7].id
            var movie_to_add = document.getElementById(clicked_id); //perform single-click action
            $("#" + clicked_id).toggleClass("adding");

  
            setTimeout(function() {
              $("#" + clicked_id).toggleClass("adding");
              seenId.push(clicked_id);
              refreshSeenMarker();
            },1000);
            

            clicks = 0;             //after action performed, reset counter

            }, DELAY);

        } else {

            clearTimeout(timer);    //prevent single-click action
            elementList = document.elementsFromPoint(event.clientX, event.clientY)
            var clicked_id = elementList[elementList.length - 7].id
            //perform double-click action
            
            if($("#" + clicked_id).hasClass('seen')){ //check if add icon is there
              $("#" + clicked_id).removeClass('seen');
              $("#" + clicked_id).toggleClass("deleting-add"); // add icon blink animation css class
            }
            
            $("#" + clicked_id).toggleClass("deleting");

            setTimeout(function() {

                if($("#" + clicked_id).hasClass('deleting-add')){
                  $("#" + clicked_id).removeClass('deleting-add'); // remove add icon blink animation css class
                }

                $("#" + clicked_id).toggleClass("deleting");
                seenId = arrayToUnique(removeAFromArray(seenId,clicked_id));
                refreshSeenMarker();
            },1000);    

            clicks = 0;             //after action performed, reset counter
        }

    })
    .on("dblclick", function(event){
        event.preventDefault();  //cancel system double-click event
    });

});


var seenId = [];
function refreshSeenMarker(){
  seenId = arrayToUnique(seenId);
  $('.darken').removeClass('seen');
  for (var i in seenId) {
    id = seenId[i];
    $("#" + id).toggleClass('seen');
  };

}

function arrayToUnique(list) {
    var result = [];
    $.each(list, function(i, e) {
        if ($.inArray(e, result) == -1) result.push(e);
    });
    return result;
}

function removeAFromArray(arr) {
    var what, a = arguments, L = a.length, ax;
    while (L > 1 && arr.length) {
        what = a[--L];
        while ((ax= arr.indexOf(what)) !== -1) {
            arr.splice(ax, 1);
        }
    }
    return arr;
}



