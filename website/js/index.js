var seenId = []; // array that stores the movie already seen

$(document).ready(function(){

    setInterval(checkRatios,100);
    detectClicking();

    

});


// On start fancy loading image

function onReady(callback) {
    var intervalID = window.setInterval(checkReady, 500);

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
    // show('movies-container', true);
    show('loading', false);
});

// // On start fancy loading image
////////////////////////


//Click to add and delete functions



function detectClicking(){

    var DELAY = 500, clicks = 0, timer = null;

    $( ".darken" ).on("click", function(event){

        clicks++;  //count clicks

        if(clicks === 1) {

            timer = setTimeout(function() {

            elementList = document.elementsFromPoint(event.clientX, event.clientY)
            var clicked_id = elementList[elementList.length - 4].id
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
            var clicked_id = elementList[elementList.length - 4].id
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
}

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

////Click to add and delete functions

function checkRatios(){

    //check movie 2:3 raiot
    
    var div = $('.darken');
    var width = div.width();
    
    div.height(width*1.5);


    //font ratio

    var fontSize = parseInt($(".darken").height());
    
    var titleFontSize = fontSize * 0.08 + "px";
    var desFontSize = fontSize * 0.045 + "px";
    var ratingBarSize = fontSize * 0.07 + "px";
    var ratingBarFontSize = fontSize * 0.04 + "px";

    $(".movie-title-main").css('font-size', titleFontSize);
    $(".description").css('font-size', desFontSize); 
    $(".rank-num").css('font-size', desFontSize);  
    
    $(".progress").css('height', ratingBarSize);
    $(".progress-bar").css('font-size', ratingBarFontSize);
    $(".progress-bar").css('line-height', ratingBarSize);

    //
    $(".movies-center-container").css('padding-top',$(".my-header").height()*1.3);

}



$(window).scroll(function () {
            var winTop = $(window).scrollTop();

            if (winTop >= $('#whole-page-container').height()*0.005) {
                $('#whole-page-container').addClass('sticky-header');
                $(".movies-center-container").css('padding-top',$(".my-header").height()*1.3);
            } else {
                $('#whole-page-container').removeClass('sticky-header');
                $(".movies-center-container").css('padding-top',$(".my-header").height()*1.3);
            }

        });

// $("body").scroll( function() {
//     var value = $(this).scrollTop();
//     if ( value > 120 )
//         $(".navbar").css("background", "transparent");
    
        
// });


