let beerHeight = 20;
let beerWidth = 200;
let beerMaxHeight = 270;
let fallingBeerHeight = 400;
let fallingBeerWidth = 20;
let fillDelay = 2;
let fillInterval = setInterval(fill, fillDelay);
let stopFillDelay = 1/100;
let stopFillingInterval = null;
let beer = null;
let fallingBeer = null;
let nbFoams = 5;
let foams = [];
let text = null;

window.onload = () => {
    beer = document.getElementById("beer");
    beer.style.height = beerHeight + "px";
    beer.style.width = beerWidth + "px";
    let beerRect = beer.getBoundingClientRect();
    fallingBeer = document.getElementById("falling_beer");
    fallingBeer.style.height = beerRect.top + "px";
    fallingBeer.style.width = fallingBeerWidth + "px";
    text = document.getElementById("text");
}

function fill(){
    beerHeight += 1;
    if(beerHeight <= beerMaxHeight && beer){
        beer.style.height = beerHeight + "px"; 
    }
    else{
        stopFill();
    }
}

function stopFill(){
    fallingBeer.style.height = 0 + "px";
    text.style.opacity = 1.0;
}

