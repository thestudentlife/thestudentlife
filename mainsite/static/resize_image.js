

function resize(){
    var maxWidth =$('.article_content').width();
    $('.article_content img').each(function(){
    var $img = $(this);
    var imgRatio = $img.width()/$img.height();
        console.log($img.width());
    $img.width(maxWidth*3/4);
        console.log($img.width());
    $img.height($img.width()/imgRatio);
    });
}

new ResizeSensor(jQuery('.article_content'), resize);

resize();
