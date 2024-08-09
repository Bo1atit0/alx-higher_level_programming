$(document).ready(function () {
  function helloTranslate () {
    const langCode = $('#language_code').val();
    const urlApi = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;

    $.get(urlApi,
      function (data) {
        $('#hello').text(data.hello);
      }
    );
  }

  $('#btn_translate').click(function () {
    helloTranslate();
  });

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      helloTranslate();
    }
  });
});
