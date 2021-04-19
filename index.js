$(document).ready(function () {

	$.post(
		"/prenota/date", function(result) {
			select = document.getElementById("dates")
			for (let i = 0; i < result.number_of_dates; i++) {
				option = document.createElement("option")
				option.text = result.dates[i]
				select.add(option)
			}
		}
	)

	$("#submit").click(function () {
		console.log("Cliccato");
		let data = {};
		data.nome = document.getElementById("fname").value;
		data.cognome = document.getElementById("lname").value;
		$.post(
			"/prenota", data, function (result) {
				print(result)
			}
		)
	})
})