
var count = 11;
var current_url = window.location.href;
var loading = false;

$(window).scroll(function(){
    if($(window).scrollTop()+window.innerHeight > $(document).height()-100){
        if(!loading){
            loading = true;
            $.ajax({
                url: current_url+"?count="+count,
                success: function(articles) {
                    console.log('ajax success');
                    loading = false;
                    count = count + 10;
                    for(a in articles) {
                        article = articles[a];
                        $(process(article)).hide().appendTo('.article_ls').show('slow');
                    }
                },
                error: function(xhr,message,exception){
                    console.log(exception);
                    loading = false;
                }
            })
        }
    }
})

String.prototype.supplant = function (o) {
    return this.replace(/{([^{}]*)}/g,
        function (a, b) {
            var r = o[b];
            return typeof r === 'string' || typeof r === 'number' ? r : a;
        }
    );
};

function process(article){
        return "<article>" +
            "<hgroup>" +
            "<h1 class='article_title'><a href='{url}'>{title}</a>".supplant({url:article['url'],title:article['title']})+"</h1>" +
            "<h2 class='article_category'><a href='{url}'>{section}</a>".supplant({url:article['section']['url'],section:article['section']['name']})+"</h2>" +
            "<h2 class='article_updated_date'>"+article['published_date']+"</h2>" +
            "</hgroup>" +
            "<p class='article_content'>{content}</p>".supplant({content:article['content']})+"" +
            "</article>";
}

