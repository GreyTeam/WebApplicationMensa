/*Made by Davide Andreolli, Daniel Francisci, Gasperetti lorenzo, Devid Troka */

$(document).ready(function () {
    $.ajax({
        url:"/classi/lista",
        type:"POST",
        headers: { 
            "Accept" : "application/json; charset=utf-8",
            "Content-Type": "application/json; charset=utf-8",
            "key": getCookie("key"),
        },
        dataType:"json",
        success: function(result) {
            select = document.getElementById("classi")
            result.classi = result.classi.sort()
            for (let i = 0; i < result.classi.length; i++) {
                console.log(result.classi[i])
                option = document.createElement("option")
                option.text = result.classi[i]
                option.value = result.classi[i]
                option.classList.add("option")
                select.add(option)    
            }
            $('body').addClass('loaded');
        }
    })

    $("#send").click(function () {
        $.ajax({
            url:"/classi/salva",
            type:"POST",
            headers: { 
                "Accept" : "application/json; charset=utf-8",
                "Content-Type": "application/json; charset=utf-8",
                "key": getCookie("key"),
                "classe": document.getElementById("classi").value
            },
            dataType:"json",
            success: function(result) {
                if (result.result == "OK")
                    window.location.replace("index_home.html")
            }
        })
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

/*Made by Davide Andreolli, Daniel Francisci, Gasperetti lorenzo, Devid Troka */