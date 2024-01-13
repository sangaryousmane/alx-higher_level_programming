// Change header color on a click with jquery

const redHeader = $('#red_header');
redHeader.on('click', function(){
	$('header').css({'color': '#FF0000'})
});
