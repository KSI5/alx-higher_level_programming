$(document).ready(function () {
  // When the document is fully loaded and ready...

  $('INPUT#btn_translate').click(function () {
    // When the button with id "btn_translate" is clicked...

    $('DIV#hello').empty();
    // Clear the content of the <div> with id "hello" to prepare for a new translation.

    const len = $('INPUT#language_code').val();
    // Get the value entered in the input field with id "language_code" and store it in the variable 'len'.

    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=' + len,
      // Make an AJAX GET request to the specified URL, including the 'len' (language code) in the query string.

      success: function (data) {
        // When the request is successful...

        $('DIV#hello').append(data.hello);
        // Append the 'hello' translation from the API response to the <div> with id "hello."
      }
    });
  });
});
