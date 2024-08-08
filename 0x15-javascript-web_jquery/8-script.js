$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function (result) {
    for (const i of result.results) {
      const item = $('<li></li>').text(i.title);
      $('UL#list_movies').append(item);
    }
  }
});
