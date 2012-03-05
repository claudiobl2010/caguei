$(document).ready(function() {

	$('#btn-caguei a').click(function() {
	        $.ajax({
				type: "POST",
				url: "/cagar",
				data: {url: $('#iframe-compartilhar').attr("src")},
				dataType: "json",
				success: function(response) {
					if (response.tipo == "SUCCESS") {

						$('#btn-caguei').html("caguei");
						$('#qtd-caguei').html(response.msg);
					}
					else {
						$('#msg-caguei').html(response.tipo + ' = ' + response.msg);
					}
				},
				error: function() {
					$('#msg-caguei').html("Ocorreu um erro. Tente novamente!!!");
				}
	        });
		return false;
	});

});
