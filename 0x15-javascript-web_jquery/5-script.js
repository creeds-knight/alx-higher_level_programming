// Adds to a list of elements

$('DIV#add_item').click(function () {
  // Append the new <li> element to UL.my_list
    $('UL.my_list').append('<li>Item</li>');
});
