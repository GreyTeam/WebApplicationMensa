$(document).ready(function () {

	$.post(
		"/prenota/date", function(result) {
			console.log(result)
			select = document.getElementById("dates")
			for (let i = 0; i < result.number_of_dates; i++) {
				option = document.createElement("option")
				option.text = result.dates[i].text
				option.value = result.dates[i].value
				option.classList.add("option")
				select.add(option)
			}
		}
	)

	$("#submit").click(function () {
		date = document.getElementById("dates").value;
        key = getCookie("key")
        console.log(key)
        $.ajax({
            url:"/prenota",
            type:"POST",
            headers: { 
                "Accept" : "application/json; charset=utf-8",
                "Content-Type": "application/json; charset=utf-8",
                "x-date": date,
                "key": key
            },
            dataType:"json",
            success: function (result) {
                console.log(result)
                if (result.result == "OK") {
                    document.cookie = "key=" + key;
                    window.location.replace("index_home.html");
                }
                else console.log("Errore")
            }
        })
	})
})

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        string = parts.pop().split(';').shift()
        string = string.slice(0, string.length - 7)
        return string
    }
}