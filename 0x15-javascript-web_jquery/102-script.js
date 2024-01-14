// fetches and prints how to say “Hello” depending on the language

$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    const languageCode = $('#language_code').val();

    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      method: 'GET',
      data: { lang: languageCode },
      dataType: 'json',
      success: function (data) {
        $('#hello').text(data.hello);
      },
      error: function (err) {
        console.error(err);
        $('#hello').text('Error fetching translation');
      }
    });
  });
});
