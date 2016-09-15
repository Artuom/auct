$(function(){

    var a = $("#makeabet").text();
    var pk = $("#pk").text();
    $("#makeabet").click(function() {
        //$('#test').text('You update it!');

    $.ajax({
        url: '/make_bet/',
        data: {
          'pk': pk
        },
        dataType: 'json',
        success: function (data) {
          $("#current_price").text(data.current_price.toFixed(2));
        }
          });
     });
});