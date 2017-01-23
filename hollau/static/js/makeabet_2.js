jQuery(document).ready(function($) {

    // для всех элементов, которые имеют атрибут data-timer, выполняем следующее действие
    $("[data-timer]").each(function () {

        // текущий элемент, обернутый в jquery
        var $this = $(this);
        var a = ($(this).find("button#makeabet"));
        var pk = ($(this).find("p#pk")).text();
        var cur_price = ($(this).find("p#current_price"));
        //var help = ($(this).find("p#help_for_bet"));
        var help = ($(this).find("button"));
        console.log(help.text());
        var betuser = ($(this).find("p#betuser"));
        
    a.click(function() {
    $.ajax({
        url: '/make_bet/',
        data: {
          'pk': pk
        },
        dataType: 'json',
        success: function (data) {
          if (data.current_price){
              cur_price.text(data.current_price.toFixed(2));
              betuser.text('Ставка от пользователь: ' + data.betuser);
          }
          else {
              help.text("Вы не можете сделать ставку!");
              help.css('background','#f00');
            }
        }
          });
     });
        
        
        
        
    });
	}); 
