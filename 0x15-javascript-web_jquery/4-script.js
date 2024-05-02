// toggles the header class when user clicks DIV#toggle_header

$('DIV#toggle_header').click(function () {
  // Toggle the "red" and "green" classes on the <header> element
    $('HEADER').toggleClass('red green');
});
