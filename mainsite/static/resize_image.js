function resize() {
    var maxWidth = $('.article_content > p').width();
    $('.article_content img').each(function () {
        var $img = $(this);
        var imgRatio = $img.width() / $img.height();
        if (imgRatio > 1) {
            $img.width(maxWidth);
            $img.height($img.width() / imgRatio);
        } else {
            $img.width(0.7 * maxWidth);
            $img.height($img.width() / imgRatio);
        }
    });
}

new ResizeSensor(jQuery('.article_content'), resize);
resize();

