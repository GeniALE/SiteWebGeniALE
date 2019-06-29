var beerHeight = 20;
var beerWidth = 200;
var beerMaxHeight = 270;
var fallingBeerHeight = 400;
var fallingBeerWidth = 20;
var fillDelay = 2;
var fillInterval;
var stopFillDelay = 1 / 100;
var stopFillingInterval = null;
var beer = null;
var fallingBeer = null;
var nbFoams = 5;
var foams = [];
var text = null;


function fill() {
    beerHeight += 1;
    if (beerHeight <= beerMaxHeight && beer) {
        beer.style.height = beerHeight + "px";
    } else {
        stopFill();
    }
}

function stopFill() {
    fallingBeer.style.height = 0 + "px";
    //text.style.opacity = 1.0;
}


$(document).ready(function () {
    beer = document.getElementById("beer");
    beer.style.height = beerHeight + "px";
    beer.style.width = beerWidth + "px";
    var beerRect = beer.getBoundingClientRect();
    fallingBeer = document.getElementById("falling_beer");
    debugger;
    fallingBeer.style.height = beerRect.top + "px";
    fallingBeer.style.width = fallingBeerWidth + "px";
    text = document.getElementById("text");

    fillInterval = setInterval(fill, fillDelay);
});
