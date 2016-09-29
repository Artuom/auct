jQuery(document).ready(function($) {

    // для всех элементов, которые имеют атрибут data-timer, выполняем следующее действие
    $("[data-timer]").each(function () {

        // текущий элемент, обернутый в jquery
        var $this = $(this);
        var ts = $this.data('timer');
        ts = new Date(ts);
        var note = $(this).find('p#note');
        
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

//});
        
        
        
        
    });
	}); 
