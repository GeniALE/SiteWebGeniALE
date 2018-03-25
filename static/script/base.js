$(document).ready(function() {
    $(".button__hamburger").click(toggleNav);
});

function toggleNav() {
    $(".button__hamburger").toggleClass("button__hamburger--close");
    $("nav.nav--fullscreen").toggleClass("nav--open");
}
