$(document).ready(function() {

	$(".item-menu").mouseover(function() {
		$(this).css("border-top-color", "#FFFFFF");
	}).mouseout(function() {
		$(this).css("border-top-color", "#3B5998");
	});

	$("#btn-caguei").mouseover(function() {
		$(this).css("border-color", "#9DACCE");
	}).mouseout(function() {
		$(this).css("border-color", "#CAD4E7");
	});

});