const date = new Date();
var selected = []

const renderCalendar = () => {
  	date.setDate(1);

	const monthDays = document.querySelector(".days");

	const lastDay = new Date(
		date.getFullYear(),
		date.getMonth() + 1,
		0
	).getDate();

  const prevLastDay = new Date(
    date.getFullYear(),
    date.getMonth(),
    0
  ).getDate();

  const firstDayIndex = date.getDay();

  const lastDayIndex = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDay();

  const nextDays = 7 - lastDayIndex - 1;

	const months = [
		"Gennaio",
		"Febbraio",
		"Marzo",
		"Aprile",
		"Maggio",
		"Giugno",
		"Luglio",
		"Agosto",
		"Settembre",
		"Ottobre",
		"Novembre",
		"Dicembre",
	];

	document.querySelector(".date h1").innerHTML = months[date.getMonth()];

	let days = "";

	$.ajax({
		url:"/admin/dates",
		type:"POST",
		headers: { 
			"Accept" : "application/json; charset=utf-8",
			"Content-Type": "application/json; charset=utf-8",
			"set": "false"
		},
		dataType:"json",
		success: function(result) {
			if (result.result == "OK") {
				selected = result.dates;
				setupDates()

				$(".dates_clickable").click(function () {
					_ = this.innerText + "/" + formatForData(date.getMonth() + 1) + "/" + (date.getYear() - 100)
					if (!selected.includes(_))
						selected.push(_);
					else 
						selected.splice(selected.indexOf(_), 1)
						
					this.classList.toggle("selected")
				})
			}
		}
	})

	document.querySelector(".prev").addEventListener("click", () => {
		date.setMonth(date.getMonth() - 1);
		renderCalendar();
	});

	document.querySelector(".next").addEventListener("click", () => {
		date.setMonth(date.getMonth() + 1);
		renderCalendar();
	});

	function setupDates() {

		for (let x = firstDayIndex; x > 0; x--) {
			days += `<div class="prev-date">${prevLastDay - x + 1}</div>`;
		}

		for (let i = 1; i <= lastDay; i++) {
			text = (formatForData(i) + "/" + formatForData(date.getMonth() + 1) + "/" + (date.getYear() - 100)).toString()
			if (selected.includes(text)) {
				days += `<div class="dates_clickable selected">${i}</div>`;
			}
			else	
				days += `<div class="dates_clickable">${i}</div>`;
		}

		for (let j = 1; j <= nextDays; j++) {
			days += `<div class="next-date">${j}</div>`;
			monthDays.innerHTML = days;
		}
	};

	return;
}


function formatForData(data) {
	if (data < 10)
		data = "0" + data.toString()
	return data.toString()
}
    
$(document).ready(() => {

	renderCalendar();

	$("#send").click(function () {
		$.ajax({
			url:"/admin/dates",
			type:"POST",
			headers: { 
				"Accept" : "application/json; charset=utf-8",
				"Content-Type": "application/json; charset=utf-8",
				"set": "true"
			},
			dataType:"json",
			data: JSON.stringify(selected),
			success: function(result) {
				if (result.result == "OK")
					alert("Date aggiornate correttamente")
			}
		
		})
	})

	$("#download").click(function () {
		console.log("result")
		$.ajax({
			url:"/admin/prenotazioni",
			type:"GET",
			dataType: 'binary',
			headers: {},
    		processData: false,
			success: function(result) {
				
			},
			failure: function(result) {
				console.log(result)
			}
		})
		console.log("Finito")
	})
	
})

