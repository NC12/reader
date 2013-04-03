$(document).ready(function() {
	$('#content').fadeIn('slow');
    // gets json data
    $.getJSON('feed.json', function(data) {
   	// loops through data
       $.each(data, function(key, value) {
       	// writes json data to html
          var news = "<section>" +
		  "<a href=" + value.link + ">" + value.title + "</a>" +
		  "<p>" + value.description + "</p>" +
		  "</section>"
          $(news).appendTo("#content article");
		});
	});
});
