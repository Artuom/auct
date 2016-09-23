jQuery(document).ready(function($) {

    // для всех элементов, которые имеют атрибут data-timer, выполняем следующее действие
    $("[data-timer]").each(function () {

        // текущий элемент, обернутый в jquery
        var $this = $(this);
        var a = ($(this).find("button#makeabet"));
        var pk = ($(this).find("p#pk")).text();
        var cur_price = ($(this).find("p#current_price"));
        var help = ($(this).find("p#help_for_bet"));
        
    a.click(function() {
    $.ajax({
        url: '/make_bet/',
        data: {
          'pk': pk
        },
        dataType: 'json',
        success: function (data) {
          if (data.cur_price){
              cur_price.text(data.current_price.toFixed(2));
          }
          else {
              help.text("Вы не можете сделать ставку!");
            }
        }
          });
     });
        
        
        
        
    });
	}); 
