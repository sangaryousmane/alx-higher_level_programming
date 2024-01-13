// Fetch and display starwars characters with jquery ajax call

$.ajax({
	url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
	method: 'GET',
	dataType: 'json',
	success: function(data) {
		$('#character').text(data.name);
	},
	error: function(err){
		console.error(err);
	}
})
