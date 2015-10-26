
$(" .article_content img").each(function() {
    var imageCaption = $(this).attr("alt");
    if (imageCaption != '') {
        var imgWidth = $(this).width();
        var imgHeight = $(this).height();
        var position = $(this).position();
        $("<br><span class='img-caption'><em>" + imageCaption +
            "</em></span>").insertAfter(this);
    }
});