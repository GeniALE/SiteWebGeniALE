// Member
$col = $("<div class='member__col'></div>");
for (i = 0; i < 7; i++) {
  $col.append($("<div class='member__square'></div>"));
}

function memberbg() {
  var random = Math.round(Math.random() * $(".member__square").length);
  var opacity = Math.random() * 0.5 + 0.5;
  setTimeout(function() {
        $(".member__square:eq("+ random +")").css("opacity", opacity);
        memberbg();
  }, 10);
}

function adjustmember() {
  var nbCol = Math.round($('.member__background').width() / 100) + 4;
  var currentNb = $('.member__col').length;
  if (currentNb < nbCol) {
    for (i = currentNb; i < nbCol; i++) {
      $('.member__bgContainer').append($col.clone());
    }
  } else if (currentNb > nbCol) {
    for (i = currentNb; i > nbCol; i--) {
      $('.member__col:last-of-type').remove();
    }
  }
}

$(document).ready(function() {
  adjustmember();
  memberbg();
  console.log("hello");
});

$( window ).resize(function() {
  adjustmember();
});
