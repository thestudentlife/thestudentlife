
var count = 11;
var current_url = window.location.href;
var loading = false;

$(window),scroll(function(){
    if($(window).scrollTop()+window.innerHeight > $(document).height()-100){
        if(!loading){
            loading = true;
            $.ajax({
                url: current_url+"?count="+count,
                success: function(articles) {
                    console.log('ajax success');
                    loading = false;
                    count = count + 10;
                    process(articles);
                },
                error: function(xhr,message,exception){
                    console.log(exception);
                    loading = false;
                }
            })
        }
    }
})



