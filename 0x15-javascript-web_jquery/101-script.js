// This script that adds, removes and clears -
// li elements from a list when the user clicks

$(document).ready(function () {
  const myList = $('ul.my_list');

  $('#add_item').on('click', () => myList.append('<li>Item</li>'));

  $('#clear_list').on('click', () => myList.empty());

  $('#remove_item').on('click', () => $('ul.my_list li:last-child').remove());
});
