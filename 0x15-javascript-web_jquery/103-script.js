$(document).ready(function () {
  function getTranslation () {
    const langCode = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
  $('INPUT#btn_translate').click(getTranslation());
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      getTranslation();
    }
  });
});
