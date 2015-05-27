var count = 11;
var current_url = window.location.href;
var loading = false;
var disqus_shortname = 'pomonatsl';

$(window).scroll(function () {
    if ($(window).scrollTop() + window.innerHeight > $(document).height() - 100) {
        if (!loading) {
            loading = true;
            $.ajax({
                       url: current_url + "&count=" + count,
                       success: function (articles) {
                           console.log('ajax success');
                           loading = false;
                           count = count + 10;
                           for (a in articles) {
                               article = articles[a];
                               var el = process(article);
                               console.log(el);
                               $('#article_ls').append(el);
                           }
                           var s = document.createElement('script'); s.async = true;
                            s.type = 'text/javascript';
                            s.src = '//' + disqus_shortname + '.disqus.com/count.js';
                            (document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
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
        " | " + article['published_date'] + " | "+
        "<i class='fa fa-comment-o'></i><a href='"+article['url']+"#disqus_thread' class='disqus_comment_count'" +
        "data-disqus-identifier='"+article['disqus_id']+"'></a>"+
        "</p>" +
        "<p class='article_content'>{content}</p>".supplant({content: article['content']}) + "" +
        "</article>" +
        "</span>";
}
