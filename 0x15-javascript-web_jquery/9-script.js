// fetches from https://hellosalut.stefanbohacek.dev/?lang=fr 
// and displays the value of hello from that fetch in the HTML tag DIV#hello.

$.ajax({
	url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
	dataType: "JSON",
	method: "GET",
	success: function(res){
		$("#hello").text(res.hello);
	},
	error: function(err){
		console.error(err);
	}
});
