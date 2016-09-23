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
        var end_date = $(this).find('p#end_date');
        ts = end_date.text();
        ts = new Date(ts);
        note = $(this).find('p#note');
        
        ($(this).find("div#countdown")).countdown({

            
		    timestamp	: ts,
		    callback	: function(days, hours, minutes, seconds){
			var message = "";
            if (days !== 0 || hours !== 0 || minutes !== 0  || seconds !== 0){
            message += days + " дней" + ", ";
			message += hours + " часов" + ", ";
			message += minutes + " минут" + " и ";
			message += seconds + " секунд" + " <br />";
			message += "осталось до завершения!";

            } else {
                message = 'Завершено!';
            }
            note.html(message);
		}
            
	});
        
        
        setInterval(function () {

        $.ajax({ 
        url: '/check_update/',
        data: {
          'pk': pk
        },
        dataType: 'json',
        success: function (data) {
            cur_price.text(data.current_price.toFixed(2));
            console.log(cur_price.text());
        
          
        }
      });
        }, 10000);
        
        
        
        
    });
    
    

   
    
	}); 


//check_update