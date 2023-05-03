$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    data.results.forEach(function (film) {
      $('<LI>').text(film.title).appendTo('UL#list_movies');
    });
  });
});
