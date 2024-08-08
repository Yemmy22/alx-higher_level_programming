/*Using Jquery-Ajax*/
/*$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function(result) {
        $('DIV#character').text(result.name);
    }
});*/

/*Using Jquery get*/
$(document).ready(function () {
    let url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
    $.get(url, function (data) {
        $('DIV#character').text(data.name);
    });
});
