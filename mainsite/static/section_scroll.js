var count = 11;
var current_url = window.location.href;
var loading = false;

$(window).scroll(function () {
    if ($(window).scrollTop() + window.innerHeight > $(document).height() - 100) {
        if (!loading) {
            loading = true;
            $.ajax({
                       url: current_url + "?count=" + count,
                       success: function (articles) {
                           console.log('ajax success');
                           loading = false;
                           count = count + 10;
                           $('#article_ls').masonry({
                                                        itemSelector: '.article-preview'
                                                    });
                           for (a in articles) {
                               article = articles[a];
                               var el = $(process(article))
                               $('#article_ls').append(el).masonry( 'appended', el, true );
                           }
                       },
                       error: function (xhr, message, exception) {
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

function author_name(authors) {
    var str = '';
    for (i in authors) {
        str = str + "<a href='" + authors[i].url + "'>" + authors[i].name + "</a>";
    }
    return str;
}

function process(article) {
    return "<span class='article-preview'>" +
        "<article>" +
        "<h3 class='article_title'><a href='{url}'>{title}</a>".supplant({
                                                                             url: article['url'],
                                                                             title: article['title']
                                                                         }) + "</h3>" +
        "<p class='article_info'>" + author_name(article.authors) +
        "|" + article['published_date'] + "</p>" +
        "<p class='article_content'>{content}</p>".supplant({content: article['content']}) + "" +
        "</article>" +
        "</span>";
}

