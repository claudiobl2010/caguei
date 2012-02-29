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
						var tmpl_html = '';
						tmpl_html += response.tipo + ' = ' + response.msg;
						tmpl_html += '<br>';
						tmpl_html += '<a href="/url/' + response.url.id + '/">Veja aqui os detalhes de sua cagada</a>';
						tmpl_html += '<br><br>';
						tmpl_html += 'COMPARTILHE<br>';
						tmpl_html += '<a href="/' + response.url.id + '">caguei</a> | twitter | facebook | google plus';
						
						$('#msg-caguei').html(tmpl_html);
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
