// Toggle between red and green with jquery

const toggleRedGreen = $('#toggle_header');
toggleRedGreen.on('click', () => $('header').toggleClass('red green'));
