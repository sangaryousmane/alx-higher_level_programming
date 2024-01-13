// Update an element text using jquery

const updateText = $('DIV#update_header');
updateText.on('click', () => $('header').text('New Header!!!'));
