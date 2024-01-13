// Add a list item on user click

const addItem = $('DIV#add_item');
addItem.on('click', () => $('UL.my_list').append('<li>Item</li>'));
