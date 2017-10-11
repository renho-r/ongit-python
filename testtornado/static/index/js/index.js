$(function() {
	$("#on").click(function() {
		$.ajax({
			method: "GET",
			url: "/led?action=on",
			dataType: "json",
			error: function(data, textStatus, jqXHR) {
				console.error(data);
			},
			success: function(data, textStatus, jqXHR) {
				console.info(data);
			}
		});
	});
	$("#off").click(function() {
		$.ajax({
			method: "GET",
			url: "/led?action=off",
			dataType: "json",
			error: function(data, textStatus, jqXHR) {
				console.error(data);
			},
			success: function(data, textStatus, jqXHR) {
				console.info(data);
			}
		});
	});
	$("#ll").click(function() {
		$.ajax({
			method: "GET",
			url: "/led?action=ll",
			dataType: "json",
			error: function(data, textStatus, jqXHR) {
				console.error(data);
			},
			success: function(data, textStatus, jqXHR) {
				console.info(data);
				data.forEach(d => {
					$("#results").append("<br>" + d);
				})
			}
		});
	});
});