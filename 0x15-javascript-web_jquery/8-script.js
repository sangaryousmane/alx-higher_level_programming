// This script fetches and lists the title for all movies 

$.ajax({
	url: "https://swapi-api.alx-tools.com/api/films/?format=json",
	method: "GET"
	dataType: "JSON",
	success: function(res){
		$('UL#list_movies').text(res.title);
	},
	error: function(err){
		console.error(err);
	}
})

