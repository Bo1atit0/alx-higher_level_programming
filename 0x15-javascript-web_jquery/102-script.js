$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    var langCode = $('INPUT#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}';

    $.get(apiUrl,
      function (data) {
        $('DIV#hello').text(data.hello);
      }
    );
  });
});
