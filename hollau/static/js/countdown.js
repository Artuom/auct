$(function(){
	var note = $('#note');
    ts = new Date(2016, 08, 13, 12, 27);
    console.log(ts + '=====');
    ts = ts.getTime();
	$('#countdown').countdown({
        
		timestamp	: ts,
		callback	: function(days, hours, minutes, seconds){
			var message = "";
            if (days !== 0 || hours !== 0 || minutes !== 0  || seconds !== 0){
            message += days + " day" + ( days==1 ? '':'s' ) + ", ";
			message += hours + " hour" + ( hours==1 ? '':'s' ) + ", ";
			message += minutes + " minute" + ( minutes==1 ? '':'s' ) + " and ";
			message += seconds + " second" + ( seconds==1 ? '':'s' ) + " <br />";
			message += "left to enddate!";
			
            } else {
                message = 'Finished';
            }
            note.html(message);
		}
	});

});