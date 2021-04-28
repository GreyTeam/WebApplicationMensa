lastSelected = ""

$(document).ready(function () {
    $.ajax({
        url:"/chronology",
        type:"POST",
        headers: { 
            "Accept" : "application/json; charset=utf-8",
            "Content-Type": "application/json; charset=utf-8",
            "key": getCookie("key"),
        },
        dataType:"json",
        success: function(result) {
    
            if (result.result == "OK") {
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
                deleteRow()
                $('body').addClass('loaded');
            }
            else document.location.replace("/index_login.html")
        }
    })

    $("#back").click(function () {
        window.location.replace("index_home.html");
	})
})

function deleteRow() {
    $("tr").click(function () {
        date = this.childNodes[0].innerText

        if (this.classList.contains("selected")) {
            lastSelected = ""
            $(".selected").slideUp(function() {
                $(this).remove();
            });
        }
        else {
            $(".selected").html(lastSelected)
            $(".selected").removeClass("selected")

            var td = document.createElement('td');
            td.colSpan = 2
            td.classList.add("cell")
            td.classList.add("selected_cell")
            td.innerText = "Eliminare?"

            this.classList.add("selected")

            lastSelected = this.innerHTML
            console.log(lastSelected)
            this.innerHTML = "";
            this.appendChild(td);
        }
    })
}

function getCookie(name) {
    const value = `;
    ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        return parts.pop().split(';').shift()
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
    return currentDate.getDate() == parsedDate.getDate();
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
