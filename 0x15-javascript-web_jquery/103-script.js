$(document).ready(function () {
  function fetchTranslation() {
    var languageCode = $('#language_code').val();

    if (languageCode.trim() !== '') {
      var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;

      $.ajax({
        url: apiUrl,
        method: 'GET',
        success: function (data) {
          if (data && data.hello) {
            $('#hello').text(data.hello);
          } else {
            console.error('Error fetching translation');
          }
        },
        error: function (error) {
          console.error('Error:', error);
        }
      });
    } else {
      console.error('Language code is empty');
    }
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
