$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (data) {
      // Make sure to clear the content of the <div> before appending the translation
      $('DIV#hello').empty().text(data.hello);
    },
    error: function () {
      // Handle errors if the request fails
      $('DIV#hello').text('Translation not available');
    }
  });
});
