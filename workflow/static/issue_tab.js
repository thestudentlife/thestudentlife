$(document).ready(function() {
    $(".articles").fadeOut(0);
    $("#News-articles").fadeIn();
});

$('.section-tab').click(function() {
    var sectionName = $(this).attr('id');
    var idName = "#" + sectionName + "-articles";
    $(".articles").not(idName).fadeOut(0, function() {
        $(idName).fadeIn();
    });
});