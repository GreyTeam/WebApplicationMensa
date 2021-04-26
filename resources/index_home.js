$.post(
    "/prenota/date", function(result) {
        console.log(result)
        select = document.getElementById("dates")
        if (result.number_of_dates == 0) {
            option = document.createElement("option")
            option.text = "Non ci sono date prenotabili"
            option.classList.add("option")
            select.add(option)
            document.getElementById("submit").disabled = true;
        }
        else {
            for (let i = 0; i < result.number_of_dates; i++) {
                option = document.createElement("option")
                option.text = result.dates[i].text
                option.value = result.dates[i].value
                option.classList.add("option")
                select.add(option)
            }
        }
    }
)

$.ajax({
	url:"/user/info",
	type:"POST",
	headers: { 
		"Accept" : "application/json; charset=utf-8",
		"Content-Type": "application/json; charset=utf-8",
		"key": getCookie("key")
	},
	dataType:"json",
	success: function (result) {
		if (result.result == "OK") {
            console.log(result)
			document.getElementById("username").innerText = "Buongiorno\n"+ result.fullname;
            searchPic = new Image();
            searchPic.src = result.profile_pic;
            console.log(searchPic);
            var _img = document.getElementById('userimage');
            _img.src = searchPic.src;
		}
		else console.log(result.message);
	}
})

$(document).ready(function () {

	$("#submit").click(function () {
		date = document.getElementById("dates").value;
        $.ajax({
            url:"/prenota",
            type:"POST",
            headers: { 
                "Accept" : "application/json; charset=utf-8",
                "Content-Type": "application/json; charset=utf-8",
                "x-date": date,
                "key": getCookie("key")
            },
            dataType:"json",
            success: function (result) {
                console.log(result)
                if (result.result == "OK") {
                    document.cookie = "key=" + getCookie("key");
                    window.location.replace("index_home.html");
                }
                else 
                    if (result.message == "A reservation for the date " + result.date + " is already registered")
                        alert("Attenzione, una prenotazione per la data " + result.date + " e' gia' stata registrata")
                    else    
                        alert(result.message)
            }
        })
	})

    $("#chronology").click(function () {
        window.location.replace("index_storico.html");
	})
})

function getCookie(name) {
    const value = `;
    ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        return parts.pop().split(';').shift()
    }
}
