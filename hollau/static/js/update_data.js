jQuery(document).ready(function($) {

    $("[data-timer]").each(function timer() {
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
     
        setInterval(function () {

        $.ajax({ 
        url: '/check_update/',
        data: {
          'pk': pk
        },
        dataType: 'json',
        success: function (data) {
            if (data.exist) {
                cur_price.text(data.current_price.toFixed(2));
            }
            else {
            }
          
        }
      });
        }, 10000);
        
        
        
        
    });
    
    

   
    
	}); 


//check_update