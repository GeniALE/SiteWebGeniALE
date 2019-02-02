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
    $('.beer__imagetag').each(function (i, el) {
        var scale = $(el).attr('data-scale');
        var pos = parseFloat($(el).attr('data-position'));

        $(el).css('transform', tagTransform(scale, pos));
    });

    $('.beer').eq(0).addClass('beer--active');
    $('.beercarousel__controls button.beercarousel__button').eq(0).addClass('beercarousel__button--active');
}

function tagTransform(scale, pos) {
    return 'scale(' + scale + ') translateX(-' + pos + '%)';
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

        var scale = $(el).attr('data-scale');
        var shift = parseFloat($(el).attr('data-position'));

        // Animate
        $(el).animate({
            dest: dest + shift
        }, {
            duration: beerTransitionTime,
            easing: 'swing',
            step: function (now, tween) {
                tween.start = origin + shift;
                $(el).css('transform', tagTransform(scale, now));
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
