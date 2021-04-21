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
                td.value = result.chronology[i];
                tr.appendChild(td);
                table.appendChild(tr);
			}
		}
    })



    $("#return").click(function () {
        window.location.replace("index_home.html");
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
