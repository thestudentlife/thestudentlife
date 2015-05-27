
var current_url = location.href

$('.facebook').click(function(){
    var share_url = "https://www.facebook.com/sharer/sharer.php?u=" + current_url;
    window.open(share_url, 545, 433);
})

$('.twitter').click(function(){
    var share_url = "https://twitter.com/home?status=" + current_url;
    window.open(share_url, 545, 433);
})

$('.google').click(function(){
    var share_url = "https://plus.google.com/share?url=" + current_url;
    window.open(share_url,545,433);
})

$('.linkedin').click(function(){
    var share_url = "https://www.linkedin.com/shareArticle?mini=true&url=" + current_url;
    window.open(share_url,545,433);
})