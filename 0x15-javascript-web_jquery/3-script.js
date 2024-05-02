// adds a class red to the header element when DIV#red_header is clicked

$('DIV#red_header').click(function () {
  // Add the "red" class to the <header> element
  $('HEADER').addClass('red');
});
