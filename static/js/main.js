$(document).ready(function() {
	$('#content').fadeIn('slow');
    $.getJSON('feed.json', function(data) {
       $.each(data, function(key, value) {
          var news = "<section>" +
		  "<a href=" + value.link + ">" + value.title + "</a>" +
		  "<p>" + value.description + "</p>" +
		  "</section>"
          $(news).appendTo("#content article");
		});
	});
});