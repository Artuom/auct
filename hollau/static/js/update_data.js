jQuery(document).ready(function($) {

    $("[data-timer]").each(function () {
        var $this = $(this);
        //console.log($this.data('timer'));
        //var ts = $this.data('timer');
        //console.log(($(this).find("div#countdown")).text());
        //console.log($("#countdown").text());
        //var note = $(this).find('p#note');
        //var a = ($(this).find("button#makeabet"));
        var pk = ($(this).find("p#pk")).text();
        //var cur_price = ($(this).find("p#current_price"));
        var cur_price = ($(this).find("p#current_price"));
        var end_date = ($(this).find('div#data-timer').data('timer'));
        console.log(cur_price);
        console.log(end_date);
        var refreshId = setInterval(function () {
        //console.log(cur_price.text());
            //data = {'end_date': lot.end_date, 'current_price': current_price}
        $.ajax({
        url: '/check_update/',
        data: {
          'pk': pk
        },
        dataType: 'json',
        success: function (data) {
          //console.log(data);
          //console.log(data.);
        }
      });
            
            
        }, 3000);
        
        
        
        
    });
	}); 
//check_update