$(document).ready(function () {
   
    key = getCookie("key"),

    $.ajax({
        url:"/chronology",
        type:"POST",
        headers: { 
            "Accept" : "application/json; charset=utf-8",
            "Content-Type": "application/json; charset=utf-8",
            "key": key
        },
        dataType:"json",
        success: function(result) {


			console.log(result.chronology)
			table = document.getElementById("table")
			for (let i = 0; i < result.chronology.length; i++) {
				var tr = document.createElement('tr');

                var td = document.createElement('td');
                td.innerText = result.chronology[i];
                td.classList.add("cell");

                var tstatus = document.createElement('td');
                status = getStatus(result.chronology[i]);
                console.log(status)
                tstatus.innerText = status;
                tstatus.classList.add("cell");
                
                tr.appendChild(td);
                tr.appendChild(tstatus);
                table.appendChild(tr);
			}
		}
    })



    $("#return").click(function () {
        window.location.replace("index_home.html");
	})
})

function getCookie(name) {
    const value = `;
    ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        string = parts.pop().split(';').shift()
        string = string.slice(0, string.length - 7)
        return string
    }
}

function parseDate(date) {
    return new Date(currentDate.getFullYear(), parseInt(date.slice(3, 5)) - 1, date.slice(0, 2));
}

function isToday(date) {
    currentDate = new Date();
    parsedDate = parseDate(date);
    console.log(currentDate);
    console.log(parsedDate);
    return currentDate.getDay() == parsedDate.getDay();
}

function getStatus(date) {
    if (isToday(date)) {
        currentTime = new Date().getHours();
        return currentTime < 8 ? "Prenotazione non inviata" : "Prenotazione arrivata"
    }
    else if (parseDate(date) > new Date())
        return "Non ancora prenotato"
    else return "Prenotazione terminata"
}