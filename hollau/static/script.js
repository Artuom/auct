$("#test_username").change(function () {
      console.log( $(this).val() );
      var username = $(this).val();

      $.ajax({
        url: '/test_ajax/',
        data: {
          'username': username
        },
        dataType: 'json',
        success: function (data) {
          console.log(data.is_taken);
          if (data.is_taken) {
            $("#help_message").text('already in use');
          }
          else {
              $("#help_message").text('');
          }
        }
      });
        
    });