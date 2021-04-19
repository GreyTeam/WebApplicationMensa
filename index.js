$(document).ready(function () {
	$('#button').click(function () {
		let data = {};
		data.nome = document.getElementById("fname").value;
		data.cognome = document.getElementById("lname").value;
		$.post(
			"/prenota", data, function (result) {
				console.log(data);
			}
		)
	})
})