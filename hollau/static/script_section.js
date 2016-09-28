console.log('in script_section.js');  
$("#select_section").keyup(function () {
      console.log( $(this).val() );
      var section = $(this).val();

      $.ajax({
        url: '/section_check/',
        data: {
          'section': section
        },
        dataType: 'json',
        success: function (data) {
          if (data.value.length === 1)  {
            $("#help_message_for_section").html('<a href="' + '">'+value+'</a>');
          }
          else {
              $("#help_message_for_section").text('Такого раздела нет');
          }
        }
      });
        
    });