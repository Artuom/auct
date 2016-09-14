$('#date1').datetimepicker({value:new Date() ,step:10, format: 'Y-m-d H:i'});
$('#date2').datetimepicker({value: new Date(new Date().getTime() + 24*60*60*1000) ,step:10, format: 'Y-m-d H:i'});
