var currentBeerIndex = 0;
var beerTransitionTime = 1500;
var beerNumber = 0;
var timer;
var dragThreshold = 100;
var lastRecordedContainerXPosition = 0;
initBeers();

$('.beercarousel__controls button.beercarousel__button').click(
    function () {
        activateBeer($('.beercarousel__controls button.beercarousel__button').index(this));
    }
);

$('.beercarousel__prevnextcontrols button.beercarousel__button').click(
    function () {
        var nextBeerIndex = currentBeerIndex == beerNumber - 1 ? 0 : currentBeerIndex + 1;
        if ($(this).hasClass('beercarousel__button--back')) {
            nextBeerIndex = currentBeerIndex == 0 ? beerNumber - 2 : currentBeerIndex - 1;
        }

        activateBeer(nextBeerIndex);
    }
);

function getAttrAsFloat(domElement, attrName) {
    return parseFloat($(domElement).attr(attrName).replace(',', '.'));
}

function initBeers() {
    beerNumber = $('div.beer').length;
    $('.beer__imagetag').each(function (_, el) {
        var scaleX = getAttrAsFloat(el,'data-scale-x');
        var scaleY =  getAttrAsFloat(el,'data-scale-y');

        var scale = scaleX + ', ' + scaleY;

        var shiftX =  getAttrAsFloat(el,'data-shift-x');
        var shiftY =  getAttrAsFloat(el,'data-shift-y');

        $(el).css('transform', tagTransform(scale, shiftX, shiftY));
    });

    $('.beer').eq(0).addClass('beer--active');
    $('.beercarousel__controls button.beercarousel__button').eq(0).addClass('beercarousel__button--active');

    // Activate draggable on container
    var $container = $('.beercarousel__beers');

    $container.draggable({
        axis: 'x',
        handle: '.beer__image',
        stop: function () {
            checkDrop($container.position().left)
        }
    });
}

function checkDrop(newPosition) {
    var difference = Math.abs(lastRecordedContainerXPosition - newPosition);
    var newIndex = currentBeerIndex;

    // Check if it is over the threshold
    if (difference > dragThreshold) {
        // Get the new index
        newIndex += lastRecordedContainerXPosition > newPosition ? 1 : -1;

        // Clamp index
        newIndex = Math.min(Math.max(newIndex, 0), beerNumber - 1);
    }

    activateBeer(newIndex);
}

function tagTransform(scale, x, y) {
    return 'scale(' + scale + ') translateX(-' + x + '%) translateY(' + y + '%)';
}

function activateBeer(index) {
    if (currentBeerIndex === index) {
        $('.beercarousel__beers').css('left', index * -100 + 'vw');
        return;
    }

    $('.beer__imagetag').each(function (i, el) {
        $(el).stop();
        var origin = 2 / 3 * 100;
        var dest = 0;

        if (currentBeerIndex < index) {
            origin = 0;
            dest = 2 / 3 * 100;

            if (index < i || i < currentBeerIndex) {
                return;
            }
        } else if (currentBeerIndex < i || i < index) {
            return;
        }

        var scaleX =  getAttrAsFloat(el,'data-scale-x');
        var scaleY =  getAttrAsFloat(el,'data-scale-y');

        var scale = scaleX + ', ' + scaleY;

        var shiftX =  getAttrAsFloat(el,'data-shift-x');
        var shiftY =  getAttrAsFloat(el,'data-shift-y');

        // Animate
        $(el).animate({
            dest: dest + shiftX
        }, {
            duration: beerTransitionTime,
            easing: 'swing',
            step: function (now, tween) {
                tween.start = origin + shiftX;
                $(el).css('transform', tagTransform(scale, now, shiftY));
            },
            complete: function () {
                timer = 0;

                // update container position
                lastRecordedContainerXPosition = $('.beercarousel__beers').position().left;
            }
        });
    });

    $('.beer').removeClass('beer--active');
    $('.beercarousel__controls button.beercarousel__button').removeClass('beercarousel__button--active');

    $('.beercarousel__beers').css('left', index * -100 + 'vw');
    $('.beer').eq(index).addClass('beer--active');
    $('.beercarousel__controls button.beercarousel__button').eq(index).addClass('beercarousel__button--active');
    currentBeerIndex = index;
}
