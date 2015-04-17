$(document).ready(function() {
    $(".articles").fadeOut(0);
    $("#News-articles").fadeIn();
});

$('.section-tab').click(function() {
    var sectionName = $(this).attr('id');
    $(".articles").fadeOut();
    var idName = "#" + sectionName + "-articles";
    $(idName).fadeIn();
});