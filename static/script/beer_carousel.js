var currentBeerIndex = 0;
var beerTransitionTime = 1500;
var beerNumber = 0;
var timer;
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
            nextBeerIndex = currentBeerIndex == 0 ? beerNumber - 2 : currentBeerIndex -1;
        }

        activateBeer(nextBeerIndex);
    }
);

function initBeers() {
    beerNumber = $('div.beer').length;
    $('.beer__imagetag').each(function (_, el) {
        var scaleX = parseFloat($(el).attr('data-scale-x'));
        var scaleY = parseFloat($(el).attr('data-scale-y'));

        var scale = `${scaleX}, ${scaleY}`;

        var shiftX = parseFloat($(el).attr('data-shift-x'));
        var shiftY = parseFloat($(el).attr('data-shift-y'));

        $(el).css('transform', tagTransform(scale, shiftX, shiftY));
    });

    $('.beer').eq(0).addClass('beer--active');
    $('.beercarousel__controls button.beercarousel__button').eq(0).addClass('beercarousel__button--active');
}

function tagTransform(scale, x, y) {
    return 'scale(' + scale + ') translateX(-' + x + '%) translateY(' + y + '%)';
}

function activateBeer(index) {
    if (currentBeerIndex === index) {
        return;
    }

    $('.beer__imagetag').each(function (i, el) {
        $(el).stop();
        var origin = 2/3*100;
        var dest = 0;

        if (currentBeerIndex < index) {
            origin = 0;
            dest = 2/3*100;

            if (index < i || i < currentBeerIndex) {
                return;
            }
        } else if (currentBeerIndex < i || i < index) {
            return;
        }

        var scaleX = parseFloat($(el).attr('data-scale-x'));
        var scaleY = parseFloat($(el).attr('data-scale-y'));

        var scale = `${scaleX}, ${scaleY}`;

        var shiftX = parseFloat($(el).attr('data-shift-x'));
        var shiftY = parseFloat($(el).attr('data-shift-y'));

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
