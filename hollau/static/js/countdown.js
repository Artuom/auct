$(function(){
	var note = $('#note');
    var text_date = $("#end_date").text();
    ts = new Date(text_date);
    ts = ts.getTime();

	$('#countdown').countdown({

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

});