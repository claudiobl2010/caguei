$(document).ready(function() {

	$('#btn-caguei').click(function() {
		if ($('#url-caguei').val() == "") {
			$('#msg-caguei').html("URL deve ser preenchida!!!");
		}
		else {
	        $.ajax({
				type: "POST",
				url: "/cagar",
				data: {url: $('#url-caguei').val()},
				dataType: "json",
				success: function(response) {
					//$('#msg-caguei').html(response.msg);
					if (response.tipo == "SUCCESS") {
						$('#msg-caguei').html(response.tipo + ' = ' + response.msg);
					}
					else {
						$('#msg-caguei').html(response.tipo + ' = ' + response.msg);
					}
				},
				error: function() {
					$('#msg-caguei').html("Ocorreu um erro. Tente novamente!!!");
				}
	        });
		}
		return false;
	});

});
