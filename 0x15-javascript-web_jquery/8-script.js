// This script fetches and lists the title for all movies

$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  dataType: 'JSON',
  success: function (res) {
    const movies = res.results;
    movies.forEach(movie => {
      $('ul#list_movies').append('<li>' + movie.title + '</li>');
    });
  },
  error: function (err) {
    console.error(err);
  }
});
