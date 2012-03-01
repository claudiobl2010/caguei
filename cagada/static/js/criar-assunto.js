$(document).ready(function() {

	$('#btn-criar').click(function() {
		if ($('#id-assunto').val() == "") {
			$('#msg-criar').html("Assunto deve ser preenchido!!!");
		}
		else {
	        $.ajax({
				type: "POST",
				url: "/cagar-assunto",
				data: {assunto: $('#id-assunto').val()},
				dataType: "json",
				success: function(response) {
					if (response.tipo == "SUCCESS") {

						var tmpl_html = '';
						tmpl_html += response.tipo + ' = ' + response.msg;
						tmpl_html += '<br>';
						tmpl_html += '<a href="/assunto/' + response.assunto.id + '/">Veja aqui os detalhes de sua cagada</a>';
						tmpl_html += '<br><br>';
						tmpl_html += 'COMPARTILHE<br>';
						tmpl_html += '<a href="/assunto/' + response.assunto.id + '">caguei</a> | twitter | facebook | google plus';
						
						$('#msg-criar').html(tmpl_html);
					}
					else {
						$('#msg-criar').html(response.tipo + ' = ' + response.msg);
					}
				},
				error: function() {
					$('#msg-criar').html("Ocorreu um erro. Tente novamente!!!");
				}
	        });
		}
		return false;
	});

});
