jQuery(document).ready(function($) {

    // для всех элементов, которые имеют атрибут data-timer, выполняем следующее действие
    $("[data-timer]").each(function () {

        // текущий элемент, обернутый в jquery
        var $this = $(this);
        //console.log($this.data('timer'));
        //var ts = $this.data('timer');
        //console.log(($(this).find("div#countdown")).text());
        //console.log($("#countdown").text());
        //var note = $(this).find('p#note');
        var a = ($(this).find("button#makeabet"));
        var pk = ($(this).find("p#pk")).text();
        var cur_price = ($(this).find("p#current_price"));
        
    a.click(function() {
    $.ajax({
        url: '/make_bet/',
        data: {
          'pk': pk
        },
        dataType: 'json',
        success: function (data) {
          cur_price.text(data.current_price.toFixed(2));
        }
          });
     });
        
        
        
        
    });
	}); 
