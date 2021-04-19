$(document).ready(function () {
	$('#button').click(function () {
		$.post(
			"/prenota", function (result) {
				console.log(result);
			}
		)
	})
})