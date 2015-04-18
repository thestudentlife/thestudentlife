$(document).ready(function() {
    $(".articles").fadeOut(0);
    $(".articles:first").fadeIn();
    $("#sectionNavigation li:first").addClass("active");
});

$('.section-tab').click(function() {
    var sectionName = $(this).attr('id');
    var idName = "#" + sectionName + "-articles";
    $('.section-tab').removeClass("active");
    $('#' + sectionName).addClass("active");
    $(".articles").not(idName).fadeOut(0, function() {
        $(idName).fadeIn();
    });
});