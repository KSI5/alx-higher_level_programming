$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function (data) {
    var movieList = data.results;
    var $listMovies = $('ul#list_movies');

    $.each(movieList, function (index, movie) {
      $listMovies.append('<li>' + movie.title + '</li>');
    });
  },
  error: function () {
    // Handle errors if the request fails
    console.error('Failed to fetch movie titles');
  }
});
