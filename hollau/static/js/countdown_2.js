jQuery(document).ready(function($) {

    // для всех элементов, которые имеют атрибут data-timer, выполняем следующее действие
    $("[data-timer]").each(function () {

        // текущий элемент, обернутый в jquery
        var $this = $(this);
        
        console.log($this.data('timer'));
        var ts = $this.data('timer');
        
        
        
        $this.countdown({
            // Берём дату из заранее заготовленной
            until: date,

            // Определяем шаблон вывода
            layout:'{desc}<span>{d<}{dn} {dl} и {d>}'+ 
            '{hn} {hl}, {mn} {ml}, {sn} {sl}</span>',

            // Определяем описание
            description: timerDescription 

            // Ну и про язык не забываем
        });

    });
	}); 
