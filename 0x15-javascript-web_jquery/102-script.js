$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;
    $.getJSON(url, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
