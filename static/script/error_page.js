var beerHeight = 20;
var beerWidth = 200;
var beerMaxHeight = 270;

var beerFillingWidth = 20;
var fillDelay = 4;
var fillInterval;

// DOM Elements
var beerFillingElem = null;
var beerElem = null;
var textElem = null;


function fill() {
    beerHeight += 1;
    if (beerHeight <= beerMaxHeight && beerElem) {
        beerElem.style.height = beerHeight + "px";
    } else {
        stopFill();
    }
}

function stopFill() {
    beerFillingElem.style.height = 0 + "px";
    textElem.style.display = "block";
    textElem.style.opacity = 1.0;
    clearInterval(fillInterval);
}

function loadHomepage() {
    location.href = location.protocol + "//" + location.host;
}

(function () {
    beerElem = document.getElementById("beer");
    beerElem.style.height = beerHeight + "px";
    beerElem.style.width = beerWidth + "px";

    var beerRect = beerElem.getBoundingClientRect();

    beerFillingElem = document.getElementById("beerFilling");
    beerFillingElem.style.height = beerRect.top - 66 + "px";
    beerFillingElem.style.width = beerFillingWidth + "px";

    textElem = document.getElementById("errorText");

    fillInterval = setInterval(fill, fillDelay);
})();