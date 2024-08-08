$(document).ready(function () {
  function fetchHello () {
    const langCode = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;

    $.getJSON(url, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('INPUT#btn_translate').click(function () {
    fetchHello();
  });

  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchHello();
    }
  });
});
