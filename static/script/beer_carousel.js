var activeBeerIndex;
activateBeer(0);

$('.beercarousel__button').click(
    function () {
        activateBeer($('.beercarousel__button').index(this));
    }
);

function activateBeer(index) {
    if (activeBeerIndex === index) {
        return;
    }
    activeBeerIndex = index;

    $('.beer').removeClass('beer--active');
    $('.beercarousel__button').removeClass('beercarousel__button--active');

    $('.beercarousel__beers').css({
        left: index * -100 + 'vw'
    });
    $('.beer').eq(index).addClass('beer--active');
    $('.beercarousel__button').eq(index).addClass('beercarousel__button--active');
}
